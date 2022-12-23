# Time Tracker

This Python script tracks the active window on your computer and logs how long each window was active for. It uses the `win32gui` and `uiautomation` libraries to retrieve the title of the active window every second. If the active window changes, it logs the duration of the previous window and starts tracking the new one.

## Features

- Tracks the active window on your computer indefinitely until interrupted by the user (e.g., by pressing `CTRL+C`).
- Handles the case where the active window is a browser (in this case, Microsoft Edge) by extracting the hostname of the website from the URL and using that as the window title instead of the browser's title.
- Writes the data to a text file with the name `activity-YYYY-MM-DD.txt`, where `YYYY-MM-DD` is the current date. The text file lists each window title and the total duration it was active for in seconds.

## Installation

To use this script, you will need to have Python 3 installed on your computer. You will also need to install the `win32gui` and `uiautomation` libraries.

To install these libraries, open a terminal and enter the following commands:
```pip install pywin32```
```pip install uiautomation```

## Usage

To run the script, open a terminal, navigate to the directory where the script is located, and enter the following command:
```python window_tracker.py```

To stop the script, press `CTRL+C`. The data for the current active window will be logged and written to the text file before the script exits.
