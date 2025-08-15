# Flet WebView Android App

This project is a complete Android application built using Python and the Flet framework. It serves as a basic web container, allowing users to browse any website within a native Android shell.

## Features

- **WebView Core**: Displays web pages as the main content.
- **Navigation Drawer**: A slide-out menu for accessing app features.
- **Change Site**: An option in the drawer to dynamically change the URL loaded in the WebView.
- **URL Persistence**: The app remembers the last visited URL and reloads it on startup.
- **Splash Screen**: A simple loading screen displayed at app launch.
- **Loading Indicator**: A progress bar is shown while web pages are loading.

---

## Installation and Setup

Follow these steps to set up the project environment.

### 1. Prerequisites

- **Python 3.7+**: Make sure Python is installed on your system. You can get it from [python.org](https://python.org).
- **Android SDK (for building and deploying)**: For building the app and installing it on a device or emulator, you will need the Android SDK Platform-Tools, which includes the Android Debug Bridge (`adb`). You can get this as part of [Android Studio](https://developer.android.com/studio) or as a separate download.

### 2. Clone the Repository

Clone this project to your local machine.

```bash
git clone <repository-url>
cd <project-directory>
```

### 3. Install Dependencies

The project dependencies are listed in the `requirements.txt` file. Install them using pip:

```bash
pip install -r requirements.txt
```

---

## Development and Testing

### Running on Desktop

You can run the application on your desktop (Windows, macOS, Linux) to quickly test its functionality without needing an Android device.

1. **Navigate to the project directory:**
   ```bash
   cd flet_android_app
   ```

2. **Run the app:**
   ```bash
   flet run main.py
   ```

---

## Building and Running on Android

### 1. Build the APK

The `flet` command-line tool packages the Python app into an Android APK file.

- **Build the APK:**
  ```bash
  flet build apk
  ```
- **(Optional) Clean previous builds:**
  Before a new build, you can clean old artifacts:
  ```bash
  flet clean
  ```

The generated APK file will be located in the `build/apk/` directory, typically named `app-release.apk`.

### 2. Running on an Android Device

- **Enable USB Debugging:** On your Android device, enable **Developer options** and **USB debugging**.
- **Connect your device:** Connect your Android device to your computer via USB.
- **Install the APK:** Use the Android Debug Bridge (`adb`) to install the app:
  ```bash
  adb install build/apk/app-release.apk
  ```

### 3. Running on an Android Emulator

- **Set up an Emulator:** Use Android Studio to create and set up an Android Virtual Device (AVD).
- **Start the Emulator:** Launch the emulator from the AVD Manager in Android Studio.
- **Install the APK:** With the emulator running, the same `adb` command will install the app on the active emulator:
  ```bash
  adb install build/apk/app-release.apk
  ```

---

## Notes

- The first build can be slow as it downloads necessary dependencies.
- For more advanced configurations, refer to the official [Flet documentation](https://flet.dev/docs/guides/python/packaging-app-for-distribution).
