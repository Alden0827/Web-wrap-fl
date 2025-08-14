# Flet Android App - Build and Run Instructions

This document provides instructions on how to build and run the Flet Android application.

## Prerequisites

- Python 3.7+
- Flet library
- Flet CLI

## Installation

1.  **Install Python:** If you don't have Python installed, download and install it from [python.org](https://python.org).

2.  **Install Flet:** Open your terminal or command prompt and install the Flet library using pip:

    ```bash
    pip install flet
    ```

## Running the Application

You can run the application on your desktop (Windows, macOS, Linux) to test its functionality.

1.  **Navigate to the project directory:**
    Open your terminal and change to the `flet_android_app` directory.

    ```bash
    cd flet_android_app
    ```

2.  **Run the app:**
    Execute the following command to run the application:

    ```bash
    flet run main.py
    ```

## Building the Android App (APK)

To build the Android application (APK), you need to have the Flet CLI installed and configured.

1.  **Clean previous builds (optional):**
    It's a good practice to clean any previous build artifacts.

    ```bash
    flet clean
    ```

2.  **Build the APK:**
    Run the following command to build the Android APK. This command will package your Flet app into an APK file that can be installed on an Android device.

    ```bash
    flet build apk
    ```

3.  **Find the APK:**
    The generated APK file will be located in the `build/apk` directory. The file will be named something like `app-release.apk`.

## Installing the APK on an Android Device

1.  **Enable USB Debugging:** On your Android device, go to **Settings > About phone** and tap on the **Build number** seven times to enable **Developer options**. Then, go to **Settings > Developer options** and enable **USB debugging**.

2.  **Connect your device:** Connect your Android device to your computer using a USB cable.

3.  **Install the APK:** Use the Android Debug Bridge (ADB) to install the APK. If you don't have ADB, you can install it as part of the Android SDK Platform-Tools.

    ```bash
    adb install build/apk/app-release.apk
    ```

    Alternatively, you can copy the APK file to your device and install it using a file manager.

## Notes

- The first build might take some time as it needs to download the necessary dependencies.
- Make sure you have a stable internet connection during the build process.
- For more advanced configurations and troubleshooting, refer to the [Flet documentation](httpshttps://flet.dev/docs/guides/python/packaging-app-for-distribution).
