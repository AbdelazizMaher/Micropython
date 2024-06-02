# ESP32 MicroPython Project

## Introduction
In this project, we will use ESP32 MicroPython to implement three functions (increment, decrement, and reset). Our range is from 0 to 9, and we will show the output on a 7-segment display. First, we will use push buttons, then control the ESP32 using Bluetooth with MIT App Inventor.
## Method 1: Using Push Buttons
Here, we use three push buttons (increment, decrement, reset).

### Steps for Getting Started with ESP32 MicroPython:

1. Installing Python 3.7.x
2. Installing Thonny IDE to program ESP32
3. Flashing the MicroPython Firmware on ESP32
4. Programming and uploading the code on ESP32 using Thonny

### 1. Installing Python 3.7.x on Windows

As MicroPython is an implementation of Python, we first need to install Python 3.7 or above.

#### Step 1
Go to this [link](https://www.python.org/downloads/) and download the latest setup of the Python installer according to your OS. Here, we are installing the Windows version.

#### Step 2
After downloading the installer, run it by double-clicking on it. When the dialog box appears, tick the "Add Python to PATH" option. Then click "Install Now" and wait until the installation process completes.

#### Step 3
After successful installation, click "Close". Python is now installed on your system.

### 2. Installing Thonny IDE on Windows to Program ESP32
To install Thonny on Windows PC, follow these instructions:

#### Step 1
Go to [Thonny.org](https://thonny.org)

#### Step 2
Download the version for Windows and wait a few seconds while it downloads.

#### Step 3
Run the .exe file and click "Install".

#### Step 4
Follow the installation wizard to complete the installation process. Click “Next” as needed.

#### Step 5
After completing the installation, open Thonny IDE. A window like the following should open:

![Thonny IDE](https://thonny.org/images/thonny_screenshot.png)

### 3. Flashing the MicroPython Firmware on ESP32
The first step is to flash our ESP32 with the MicroPython firmware. This process is similar to flashing an ESP-12e based board with the NodeMCU firmware.

#### Step 1
Download the bin file for the most recent MicroPython firmware from the [MicroPython downloads page](https://micropython.org/download/esp32/).

#### Step 2
Scroll down to where the firmware for the ESP32 boards is located, and select the one that matches your board. Click to download it.

#### Burning the Firmware
Follow these steps to burn the firmware:

1. Connect your ESP32 board to your computer via USB.
2. Open a command prompt or terminal.
3. Navigate to the directory where you downloaded the firmware.
4. Use esptool.py to erase the flash: `esptool.py --port COM3 erase_flash`
5. Flash the new firmware: `esptool.py --chip esp32 --port COM3 --baud 460800 write_flash -z 0x1000 esp32-20210902-v1.17.bin`
6. Wait for the flashing process to complete.
7. Disconnect and reconnect your ESP32 board.

### 4. Programming and Uploading Code on ESP32 using Thonny
Run Thonny IDE, write your MicroPython code, and upload it to the ESP32.

### Hardware Components
- Breadboard
- Generic ESP32 module
- 7-segment display
- 3 push buttons
- Jumper wires
- USB cable

Using the figures from the data sheet, connect your circuit as shown in the following diagram:

![Circuit Diagram](https://randomnerdtutorials.com/wp-content/uploads/2018/08/ESP32-7-Segment-wiring-diagram.png)

## Method 2: Using MIT App Inventor

### Steps for Getting Started with Using MIT App Inventor:

1. Making an Account in MIT App Inventor 2
2. Search for “MIT APP Inventor 2” on Google.

3. Click on the "Create Apps" button.
4. Sign in with your Google account.
5. Click on "Start new project" and name your project.

> The program window where you can design your app appears.

Design your app using the available components.

Find the components and their properties settings in the sidebar.
Suggested tutorial to understand the program: MIT App Inventor Tutorial

Create the code for your project in the Blocks section.

2. Installing Arduino IDE
Step-by-step installation process:

Go to the Arduino website.
Download the version for your operating system.
Run the installer and follow the installation wizard.
Open the Arduino IDE once the installation is complete.

Connect your ESP32 to your computer via a USB cable.
Select the correct board and port under 'Tools' > 'Board' and 'Port'.
Install the required libraries for ESP32.
