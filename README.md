# ESP32 Random Password Generator & Python Guessing Script

This project demonstrates an approach to password generation and brute-forcing using an ESP32 and a Python script.

## Project Overview

- **ESP32 Code:**
  - Uses a custom pseudo-random number generator (PRNG) to create a 64-character random password from a specified alphabet.
  - Responds with **TRUE** if the guessed password is correct, or **FALSE** otherwise.

- **Python Script:**
  - Connects to the ESP32 over a serial port.
  - Iterates through possible PRNG seeds to generate passwords.
  - Sends those guesses to the ESP32 in a brute-force manner.
  - When the correct password is found, the script prints a success message.

## Running the Project

### 1. Prepare the ESP32

- **Open the `.ino` file** in the Arduino IDE (or PlatformIO).
- **Select your ESP32 board** and the correct serial port under **Tools**.
- **Click Upload** to flash the code onto the ESP32.
- Once uploaded, the ESP32 will generate and store a random password in its memory.

### 2. Install Python Dependencies

- Ensure you have **Python 3** installed.
- Install **pyserial** by running:
  ```bash
  pip install pyserial
