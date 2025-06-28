# infoFrame.py
from customtkinter import CTkScrollableFrame, CTkLabel
import webbrowser


def create_info_frame(parent, width, height, corner_radius, frameBgcolor, frameFgcolor):
    info_frame = CTkScrollableFrame(parent, width=width, height=height, corner_radius=corner_radius,bg_color=frameBgcolor,fg_color=frameFgcolor)

    
    # Function to open the link
    def open_link(event=None):
        webbrowser.open_new("https://ankitprim.github.io/portfolio/")

    # Hover effects
    def on_enter(event):
        link_label.configure(text_color="#1a0dab")  # Google blue

    def on_leave(event):
        link_label.configure(text_color="blue")


    
    CTkLabel(info_frame, text="Application Info", wraplength=300, font=("Impact", 32)).pack(pady=20, padx=14, anchor="w")
    
    
    CTkLabel(info_frame,
             text="ARC* is a desktop-based email campaigning application developed using Python and the CustomTkinter GUI framework. The application is designed to simplify the process of sending bulk emails by providing a clean, user-friendly interface and essential campaign management tools. ARC* enables users to import recipient lists from CSV files, compose emails with a subject and body, and send them efficiently using SMTP. The interface is divided into modular frames—Home, Email, Help, and Info—each serving a specific function. This modular structure enhances maintainability and scalability. The app supports basic email tracking features through embedded image links, which can be extended for full analytics in future versions. ARC* is aimed at small businesses, individual marketers, and students who need a lightweight and accessible tool for managing email outreach campaigns directly from their desktop.",
             wraplength=320, justify="left", font=("Sitka Banner", 17)).pack(pady=10, padx=16, anchor="w")
    
    CTkLabel(info_frame, text="Design & Devloped by:", wraplength=300, font=("Impact", 28)).pack(pady=20, padx=14, anchor="w")
    link_label = CTkLabel(info_frame,
             text="Ankit kushwaha",
             wraplength=320, justify="left", font=("Sitka Banner", 18))
    link_label.pack(pady=0, padx=16, anchor="w")

    
    CTkLabel(info_frame, text="⚠️ Warning ⚠️",text_color="brown3", wraplength=360, font=("Impact", 28)).pack(pady=20, padx=14, anchor="w")
    CTkLabel(info_frame,
             text="""This software application, ARC* , along with its source code, graphical interface, documentation, and all associated components, is the original work of the developers: Ankit, Dharmvir, and Piyush. It is protected under applicable intellectual property and copyright laws.\n No part of this software may be reproduced, distributed, transmitted, modified, reverse-engineered, or used in any form or by any means without the prior written permission of the authors. Unauthorized duplication or use of this software for commercial or non-commercial purposes is strictly prohibited and may result in legal action.\n The developers disclaim any liability for damages resulting from the use or misuse of this application. The software is provided "as is" without warranty of any kind, either express or implied, including but not limited to the implied warranties of merchantability and fitness for a particular purpose.\n ARC* was created as an independent project with the intent to provide an efficient, desktop-based solution for bulk email campaigning and outreach.\n For permissions, suggestions, or inquiries, please contact the development team directly.""",
             wraplength=320, justify="left" ,font=("Sitka Banner", 17)).pack(pady=0, padx=16, anchor="w")
    

    CTkLabel(info_frame, text="© 2025 ARC*", wraplength=300, font=("Sitka Banner", 18)).pack(pady=0, padx=14, anchor="center")
    CTkLabel(info_frame, text=" ", wraplength=360, font=("Sitka Banner", 18)).pack(pady=0, padx=14, anchor="w")
    
    
    # Bind click and hover events
    link_label.bind("<Button-1>", open_link)
    link_label.bind("<Enter>", on_enter)
    link_label.bind("<Leave>", on_leave)
    
    return info_frame
