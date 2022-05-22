import win32gui
import uiautomation as auto
import time
from datetime import date, datetime

# Initialize these variables outside of loop so the first focused window will have something to use.
active_window_name = ""
count = 0
start_time = datetime.now()

# Get browser url, extract hostname
def get_browser_window():
    window = win32gui.GetForegroundWindow()
    browserControl = auto.ControlFromHandle(window)
    edit = browserControl.EditControl()
    website = edit.GetValuePattern().Value.split('/')
    return website[2]

# Get active window title
def get_active_window():
    window = win32gui.GetForegroundWindow()
    active_window = win32gui.GetWindowText(window)
    return active_window

# Create empty activity list
activity_list = {}

# Begin main loop
try:
    while True:
        # Get the new focused window (in first iteration, this is also the "active_window")
        new_window_name = get_active_window()
        # Check if the focused window is a browser (in this case, MS Edge)
        if "Edge" in new_window_name:
            try:
                # If it is edge, set new_window_name to the URL hostname
                # The purpose of this is to track how long you're working on a particular website.
                new_window_name = get_browser_window()
            # This will handle an error that occurs when opening a new tab that doesn't have a URL
            except IndexError:
                pass
        # Check every second to see if the new window name is the same as the active window name
        if new_window_name != active_window_name:
            # If they are not the same, log the duration and create a new dictionary entry or update an existing one
            if count != 0 or active_window_name != "":
                end_time = datetime.now()
                end_time = end_time.time()
                start_time = start_time.time()
                duration = datetime.combine(date.min, end_time) - datetime.combine(date.min, start_time)
                try:
                    activity_list[active_window_name] += duration.seconds
                except KeyError:
                    activity_list[active_window_name] = duration.seconds
            # Set the active window name to the same as the new window name and reset variables that track duration.
            active_window_name = new_window_name
            count = 0
            start_time = datetime.now()
        # If the active window name is the same as new_window_name, begin a new loop to start counting 
        else:
            while active_window_name == new_window_name:
                # Check the active window every second in order to trigger the conditional above if it changes
                new_window_name = get_active_window()
                count += 1
                print(f'{active_window_name} - {count} - start: {start_time}')
                # print(f'{active_window_name.split("-")[-1].strip()} - {count} - start: {start_time}')
                time.sleep(1)

        # time.sleep(1)       
# Listen for KeyboardInterrupt and add the last/most recent window to the dictionary with the same logic as above.
except KeyboardInterrupt:
    if count != 0 or active_window_name != "":
                end_time = datetime.now()
                end_time = end_time.time()
                start_time = start_time.time()
                duration = datetime.combine(date.min, end_time) - datetime.combine(date.min, start_time)
                try:
                    activity_list[active_window_name] += duration.seconds
                except KeyError:
                    activity_list[active_window_name] = duration.seconds
    print(activity_list)
    exit()

# TODO:
# Summarize the activity once the program exits and possibly write it to a file with today's date
# Determine best way to run app in the background and also have it able to listen for exit
# Add the ability to pause for lunch/bathroom breaks, etc...
# Possibly build a UI so it will be easier to achieve the above