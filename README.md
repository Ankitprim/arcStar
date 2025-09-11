# ARC* Email Campaign Desktop Application

## Overview
ARC* is a desktop-based email campaign application built with Python and CustomTkinter. It provides a user-friendly interface for sending bulk emails, managing campaigns, and handling recipient lists. The app is ideal for small businesses, marketers, and students who need a lightweight tool for email outreach.

## Features
- **Bulk Email Sending:** Import recipient lists from CSV/Excel files and send emails efficiently using SMTP.
- **HTML Email Support:** Compose rich HTML emails or load templates.
- **Attachments:** Easily attach files to your emails.
- **Settings Management:** Save and load sender email, subject, and message body.
- **Progress Tracking:** Visual progress bar for email sending status.
- **Modular UI:** Frames for Home, Email, Help, and Info for easy navigation.
- **Help & Info:** Built-in help for Gmail app password setup and application info.

## Getting Started
### Prerequisites
- Python 3.8+
- Required packages: `customtkinter`, `Pillow`, `pandas`, `openpyxl`

### Installation
1. Clone or download the repository.
2. Install dependencies:
	```powershell
	pip install customtkinter Pillow pandas openpyxl
	```
3. Run the application:
	```powershell
	python main.py
	```

### Gmail Setup
- **App Password:** For Gmail, generate an app password (see Help section in the app).
- **Less Secure Apps:** Not recommended, but instructions are provided in the Help frame.

## File Structure
```
arc_installer.iss         # Installer script
main.py                  # Application entry point
Home.py                  # Main GUI and frame switching
emailFrame.py            # Email campaign frame
helpFrame.py             # Help frame (Gmail setup)
infoFrame.py             # Info frame (about, credits)
logic.py                 # Core logic (email sending, file handling)
icons/                   # App icons and images
logs/settings.txt        # Saved settings
preinstall_info.txt      # Pre-installation info
LICENSE.txt              # License
README.md                # This file
```

## Usage
- Launch the app and start your campaign from the Home frame.
- Use the Email frame to enter sender details, load recipients, compose your message, attach files, and send emails.
- Save your settings for future use.
- Access Help and Info frames for guidance and credits.

## Credits
- **Design & Developed by:** Ankit Kushwaha
- **Contributors:** Dharmvir, Piyush

## License
This project is protected under copyright laws. See `LICENSE.txt` for details.

## Disclaimer
ARC* is provided "as is" without warranty. Use at your own risk. For permissions or inquiries, contact the development team.

