# emailFrame.py
from customtkinter import *
import customtkinter as ctk
from logic import *

def create_email_frame(parent, width, height, corner_radius, bg_color,frameFgcolor):
    email_frame = ctk.CTkFrame(parent, width=width, height=height, corner_radius=corner_radius, bg_color=bg_color, fg_color=frameFgcolor)

    level_font = ("Calibri Bold", 18)

    btn_color="turquoise4"
    btn_hover="lightseagreen"

    ctk.CTkLabel(email_frame, 
                 text="Start Campaign", 
                 font=("Impact", 32)).place(relx=0.08, rely=0.04)

    ctk.CTkLabel(email_frame, 
                 text="Sender Email:", 
                 font=level_font).place(relx=0.08, y=85)
    sender_email_entry = ctk.CTkEntry(email_frame, width=200)
    sender_email_entry.place(y=85, x=150)

    ctk.CTkLabel(email_frame, 
                 text="Password:", 
                 font=level_font).place(relx=0.08, y=120)
    password_entry = ctk.CTkEntry(email_frame, show="*", width=200)
    password_entry.place(y=120, x=150)

    ctk.CTkLabel(email_frame, 
                 text="Recipients (one email per line):", 
                 font=level_font).place(relx=0.08, y=160)
    
    recipient_email = ctk.CTkTextbox(email_frame, 
                                     height=110, 
                                     width=200, 
                                     wrap="word")
    recipient_email.place(y=190, x=150)

    ctk.CTkButton(email_frame, 
                  text="Load Recipients", 
                  hover_color=btn_hover,
                  fg_color=btn_color,
                  command=lambda: load_recipients(recipient_email), 
                  width=70, 
                  height=40).place(relx=0.08, rely=0.3)
    
    ctk.CTkButton(email_frame, 
                  text="Clear Recipients", 
                  command=lambda: clear_recipients(recipient_email), 
                  width=70, 
                  hover_color=btn_hover,
                  fg_color=btn_color,
                  height=40).place(relx=0.08, rely=0.37)

    ctk.CTkLabel(email_frame, 
                 text="Subject:", 
                 font=level_font).place(relx=0.08, rely=0.47)
    subject_entry = ctk.CTkEntry(email_frame, width=200)
    subject_entry.place(x=150, rely=0.47)

    ctk.CTkLabel(email_frame, 
                 text="Message Body:", 
                 font=level_font).place(relx=0.08, rely=0.52)
    ctk.CTkButton(email_frame, 
                  text="Load HTML Template", 
                  hover_color=btn_hover,
                  fg_color=btn_color,
                  command=lambda: load_html_template(message_text),
                  width=150).place(relx=0.08, rely=0.575)
    ctk.CTkButton(email_frame,
              text="Attach Files",
              command=choose_attachments,
              hover_color=btn_hover,
              fg_color=btn_color,
              width=150).place(relx=0.52, rely=0.575)


    message_text = ctk.CTkTextbox(email_frame, 
                                  height=150, 
                                  width=320, 
                                  wrap="word")
    message_text.place(relx=0.08, rely=0.63)

  
    send_button = ctk.CTkButton(email_frame, text="Send", width=90,
                                hover_color=btn_hover,
                                fg_color=btn_color,
                                command=lambda: threaded_send(sender_email_entry, password_entry, recipient_email, subject_entry, message_text, send_button, progress_bar))
    send_button.place(relx=0.08, rely=0.865)

    save_button = ctk.CTkButton(email_frame, text="Save", width=90,
                                hover_color=btn_hover,
                                fg_color=btn_color,
                                command=lambda: save_settings(sender_email_entry, subject_entry, message_text))
    save_button.place(relx=0.38, rely=0.865)

    clearAll_button = ctk.CTkButton(email_frame, text="Clear", width=90,
                                    hover_color=btn_hover,
                                    fg_color=btn_color,
                                    command=lambda: clear_all(sender_email_entry, password_entry, recipient_email, subject_entry, message_text, progress_bar))
    clearAll_button.place(relx=0.68, rely=0.865)


    progress_bar = ctk.CTkProgressBar(email_frame,
                                      progress_color=btn_color,
                                       fg_color="white", width=320)
    progress_bar.place(relx=0.08, rely=0.925)
    progress_bar.set(0)

    # Load settings on creation
    load_settings(sender_email_entry, subject_entry, message_text)

    return email_frame
