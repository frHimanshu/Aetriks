# Aetriks: Simple Python Keylogger

A simple Python keylogger that captures keystrokes and sends them to a remote server.

> **Disclaimer**:  
> This code is for **educational purposes only**! Do not use it for any illegal activities. Misuse of this tool is your responsibility.

---

## Features

- Captures keystrokes in real-time.
- Sends collected keystrokes to a remote server.
- Configurable server IP, port, and data transmission interval.

---

## Installation Guide

### **For Linux/MacOS**

1. **Clone the repository**:
   ```bash
   git clone https://github.com/frHimanshu/Aetriks.git
   cd Aetriks
   ```

2. **Create a virtual environment**:
   ```bash
   python3 -m venv keylogger_env
   source keylogger_env/bin/activate
   ```

3. **Install required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the keylogger**:
   ```bash
   python keylogger.py
   ```

---

### **For Windows**

1. **Clone the repository**:
   ```bash
   git clone https://github.com/frHimanshu/Aetriks.git
   cd Aetriks
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv keylogger_env
   keylogger_env\Scripts\activate
   ```

3. **Install required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the keylogger**:
   ```bash
   python keylogger.py
   ```

---

## Configuration

1. **Edit the `config.json` file**:
   - The keylogger uses a `config.json` file to configure the server details and data transmission interval.
   - Example `config.json`:
     ```json
     {
         "ip_address": "127.0.0.1",
         "port_number": 5000,
         "time_interval": 10
     }
     ```
   - Place this file in the same directory as `keylogger.py`.

2. **Server Setup**:
   - Use the [Aetriks Relay Server](https://github.com/frHimanshu/aetriks-relay) to handle incoming keystroke data.
   - Clone the server repository and follow its setup instructions.

---

## Legal and Ethical Use

This project is for **educational purposes only**.  
**Make sure you have explicit permission** before running this on any device. Misuse of this tool is your responsibility.

---

## Troubleshooting

- **Missing Dependencies**:  
  Ensure all dependencies are installed by running:
  ```bash
  pip install -r requirements.txt
  ```

- **Server Connection Issues**:  
  Verify the `ip_address` and `port_number` in `config.json` match the server's configuration.

- **Permission Denied**:  
  Run the script with appropriate permissions if required:
  ```bash
  sudo python keylogger.py
  ```

---

## Contribution

Feel free to contribute to this project by submitting issues or pull requests on [GitHub](https://github.com/frHimanshu/Aetriks).

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
