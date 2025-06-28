# helpFrame.py
from customtkinter import CTkFrame, CTkLabel

def create_help_frame(parent, width, height, corner_radius, frameBgcolor, frameFgcolor):
    help_frame = CTkFrame(parent, width=width, height=height, corner_radius=corner_radius,fg_color=frameFgcolor ,bg_color=frameBgcolor)

    CTkLabel(help_frame, text="Help", font=("Impact", 32)).place(x=20, rely=0.04)
    CTkLabel(help_frame, text="1. Use an App Password", font=("Calibri Bold", 18)).place(x=30, y=80)
    CTkLabel(help_frame, text="Generate an App Password:", font=("Calibri Light", 18)).place(x=35, y=105)
    CTkLabel(help_frame, text="""- Log in to your Gmail account.
- Go to Google Account Settings > Security.
- Enable 2-Step Verification.
- Under App Passwords, generate one for "Mail" on "Windows Computer".
- Use this instead of your real password.""", wraplength=330, font=("Calibri Light", 15), justify="left").place(x=35, y=130)

    CTkLabel(help_frame,
              text="2. Enable Less Secure App Access (Not Recommended)",
              wraplength=300, 
              font=("Calibri Bold", 18)).place(x=30, y=270)
    
    CTkLabel(help_frame, 
             text="- Go to Google Account Settings > Security\n- Enable Less Secure App Access.", 
             font=("Calibri Light", 15),
             justify="left").place(x=30, y=320)
    
    CTkLabel(help_frame, 
             text="Note: This option might not be available for newer accounts.", 
             wraplength=330, 
             font=("Calibri Light", 18)).place(x=35, y=370)

    return help_frame
