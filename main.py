# main.py

from Home import root
import sys
import os

# Get the base path for the executable or script
if getattr(sys, 'frozen', False):  # Running as a bundled executable
    BASE_PATH = sys._MEIPASS
else:  # Running as a script
    BASE_PATH = os.path.dirname(os.path.abspath(__file__))

# Update paths to resources
ICON_PATH = os.path.join(BASE_PATH, "icons")
SETTINGS_FILE = os.path.join(BASE_PATH, "logs")
# This is the entry point for the application.
if __name__ == "__main__":
    root.mainloop()
