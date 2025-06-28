from customtkinter import *
import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import tkinter as tk
import os
import sys
from helpFrame import create_help_frame
from infoFrame import create_info_frame
from emailFrame import create_email_frame
from logic import *

# GUI Setup
ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("green")

# Get the base directory
if getattr(sys, 'frozen', False):
    BASE_PATH = sys._MEIPASS
else:
    BASE_PATH = os.path.dirname(os.path.abspath(__file__))

# Load icons
home_icon = CTkImage(dark_image=Image.open(os.path.join(BASE_PATH, "icons", "home.png")), size=(30, 30))
email_icon = CTkImage(dark_image=Image.open(os.path.join(BASE_PATH, "icons", "mail.png")), size=(30, 30))
help_icon = CTkImage(dark_image=Image.open(os.path.join(BASE_PATH, "icons", "help.png")), size=(30, 30))
info_icon = CTkImage(dark_image=Image.open(os.path.join(BASE_PATH, "icons", "info.png")), size=(30, 30))
icon_path = os.path.join(BASE_PATH, "icons", "icon.ico")

banner_img = Image.open(os.path.join(BASE_PATH, "icons", "banner.png"))
banner_img = banner_img.resize((440, 670))



# Main Window
root = ctk.CTk()
root.title("Arc*")
root.geometry("440x670")
root.resizable(False, False)
root.iconbitmap(icon_path)

# UI Variables
menufg = "white"
menu_hoverColor = "lavender"
frameBgcolor = "white"
frameFgcolor = "lavender"
frameCornerRadius = 10
frameWidth = 380
frameHeight = 679
level_font = ("Calibri Bold", 18)


# Home Frame
home_frame = ctk.CTkFrame(root, width=440, height=frameHeight, corner_radius=frameCornerRadius, fg_color="white", bg_color=frameBgcolor)
home_frame.place(x=0, y=0)

# Convert to CTkImage (recommended for High DPI)
bg_ctk_img = CTkImage(light_image=banner_img, dark_image=banner_img, size=(440, 670))

# Apply as background
ctk.CTkLabel(home_frame, image=bg_ctk_img, text="").place(x=0, y=0, relwidth=1, relheight=1)



ctk.CTkLabel(home_frame,
    text="An Email Campaign desktop Application", 
    font=("Ink Free", 16), 
    wraplength=180).place(relx=0.08, rely=0.2)

ctk.CTkButton(home_frame, 
              text="Launch your \n Campaign", 
              font=("Impact",20),
              corner_radius=10,
              height=40,
              hover_color="maroon4",
              fg_color="turquoise4",
              command=lambda:show_emails(home_frame, help_frame, info_frame,second_frame,email_frame)).place(relx=0.07, rely=0.35)

# Second Frame 
second_frame = ctk.CTkFrame(root, 
                            width=frameWidth + 60, 
                            height=frameHeight, 
                            corner_radius=frameCornerRadius, 
                            fg_color=frameBgcolor)


# menu frame
menu_frame = ctk.CTkFrame(second_frame, 
                          width=60, 
                          height=frameHeight, 
                          fg_color=frameBgcolor)
menu_frame.place(x=0, y=0)

ctk.CTkButton(menu_frame, text="", 
              image=home_icon, 
              hover_color=menu_hoverColor, 
              command=lambda:show_home(home_frame, help_frame, info_frame,second_frame,email_frame), 
              width=40, 
              fg_color=menufg).place(x=7, y=30)

ctk.CTkButton(menu_frame, text="", 
              image=email_icon, 
              hover_color=menu_hoverColor, 
              command=lambda:show_emails(home_frame, help_frame, info_frame,second_frame,email_frame), 
              width=40, 
              fg_color=menufg).place(x=7, y=90)

ctk.CTkButton(menu_frame, text="", 
              image=help_icon, 
              hover_color=menu_hoverColor, 
              command=lambda:show_help(home_frame, help_frame, info_frame,second_frame,email_frame), 
              width=40, 
              fg_color=menufg).place(x=7, y=150)

ctk.CTkButton(menu_frame,
              text="", 
              image=info_icon, 
              hover_color=menu_hoverColor, 
              command=lambda:show_info(home_frame, help_frame, info_frame,second_frame,email_frame), 
              width=40, 
              fg_color=menufg).place(x=7, rely=0.9)




# Email Frame
email_frame = create_email_frame(second_frame, frameWidth, frameHeight, frameCornerRadius, frameBgcolor, frameFgcolor)

# Help Frame
help_frame = create_help_frame(second_frame,frameWidth, frameHeight,frameCornerRadius,frameBgcolor,frameFgcolor)

# Info Frame
info_frame = create_info_frame(second_frame,frameWidth,frameHeight,frameCornerRadius,frameBgcolor,frameFgcolor)




# Start with Home Frame 
show_home(home_frame, help_frame, info_frame,second_frame,email_frame)

root.mainloop()