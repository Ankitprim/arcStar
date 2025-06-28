from tkinter import filedialog, messagebox
import threading
import os
import sys
import smtplib
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import re
from email.mime.base import MIMEBase
from email import encoders




# Frame Switching Functions
def show_home(home_frame, help_frame, info_frame,second_frame,email_frame):
    for frame in [second_frame, email_frame, help_frame, info_frame]:
        frame.place_forget()
    home_frame.place(x=0, y=0)

def show_emails(home_frame, help_frame, info_frame,second_frame,email_frame):
    for frame in [home_frame, help_frame, info_frame]:
        frame.place_forget()
    second_frame.place(x=0, y=0)
    email_frame.place(x=60, y=0)

def show_help(home_frame, help_frame, info_frame,second_frame,email_frame):
    for frame in [home_frame, email_frame, info_frame]:
        frame.place_forget()
    second_frame.place(x=0, y=0)
    help_frame.place(x=60, y=0)

def show_info(home_frame, help_frame, info_frame,second_frame,email_frame):
    for frame in [home_frame, email_frame, help_frame]:
        frame.place_forget()
    second_frame.place(x=0, y=0)
    info_frame.place(x=60, y=0)










# Get the base path for the executable or script
if getattr(sys, 'frozen', False):  # Running as a bundled executable
    BASE_PATH = sys._MEIPASS
else:  # Running as a script
    BASE_PATH = os.path.dirname(os.path.abspath(__file__))

def load_settings(sender_email_entry, subject_entry, message_text):
    if os.path.exists(os.path.join(BASE_PATH, "logs", "settings.txt")):
        with open(os.path.join(BASE_PATH, "logs", "settings.txt"), "r") as file:
            lines = file.readlines()
            if len(lines) >= 3:
                sender_email_entry.delete(0, "end")
                sender_email_entry.insert(0, lines[0].strip())
                subject_entry.delete(0, "end")
                subject_entry.insert(0, lines[1].strip())
                message_text.delete("1.0", "end")
                message_text.insert("1.0", lines[2].strip())

def save_settings(sender_email_entry, subject_entry, message_text):
    with open(os.path.join(BASE_PATH, "logs", "settings.txt"), "w") as file:
        file.write(sender_email_entry.get() + "\n")
        file.write(subject_entry.get() + "\n")
        file.write(message_text.get("1.0","end").strip())
    messagebox.showinfo("Settings Saved", "Settings saved successfully!")


# Email validation regex function
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email)

def load_recipients(recipient_email):
    # Open CSV or Excel file
    file_path = filedialog.askopenfilename(filetypes=[("CSV or Excel Files", "*.csv *.xlsx")])

    if file_path:
        try:
            # Read CSV or Excel
            if file_path.endswith(".csv"):
                df = pd.read_csv(file_path)
            elif file_path.endswith(".xlsx"):
                df = pd.read_excel(file_path)
            else:
                messagebox.showerror("Error", "Unsupported file format.")
                return

            # Check possible column names
            possible_columns = ['Email', 'email', 'Emails', 'emails']
            email_column = next((col for col in possible_columns if col in df.columns), None)

            if not email_column:
                messagebox.showerror("Error", "No valid email column found.\nExpected: 'Email', 'email', 'Emails', or 'emails'.")
                return

            # Process emails
            raw_emails = df[email_column].dropna().astype(str).tolist()
            valid_emails = []
            invalid_emails = set()
            unique_emails = set()

            for email in raw_emails:
                email = email.strip()
                if is_valid_email(email):
                    if email not in unique_emails:
                        valid_emails.append(email)
                        unique_emails.add(email)
                else:
                    invalid_emails.add(email)

            if valid_emails:
                recipient_email.delete("1.0", "end")
                recipient_email.insert("1.0", '\n'.join(valid_emails))
                summary_msg = f"✔️ Loaded {len(valid_emails)} valid and unique email(s)."

                if invalid_emails:
                    summary_msg += f"\n⚠️ {len(invalid_emails)} invalid email(s) were skipped."
                    summary_msg += f"\n\nInvalid Emails:\n" + "\n".join(list(invalid_emails)[:5])
                    if len(invalid_emails) > 5:
                        summary_msg += "\n..."

                messagebox.showinfo("Load Complete", summary_msg)
            else:
                messagebox.showwarning("No Valid Emails", "No valid email addresses found in the file.")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to load file.\nDetails: {str(e)}")


def clear_recipients(recipient_email):
    recipient_email.delete("1.0", "end")


def load_html_template(message_text):
    file_path = filedialog.askopenfilename(filetypes=[("HTML Files", "*.html")])
    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            html_content = file.read()
            message_text.delete("1.0", "end")
            message_text.insert("1.0", html_content)



def choose_attachments():
    global attachment_paths
    attachment_paths = filedialog.askopenfilenames(
        title="Select Attachments",
        filetypes=[("All Files", "*.*")]
    )
    if attachment_paths:
        messagebox.showinfo("Attachments Added", f"{len(attachment_paths)} file(s) selected.")


attachment_paths = []  # global list to store selected file paths

def send_email(sender_email_entry, password_entry, recipient_email, subject_entry, message_text, send_button, progress_bar):
    sender_email = sender_email_entry.get()
    password = password_entry.get()
    recipients = recipient_email.get("1.0", "end").strip().split("\n")
    subject = subject_entry.get()
    message_body = message_text.get("1.0", "end").strip()

    if not sender_email or not password or not recipients or not subject or not message_body:
        messagebox.showwarning("Warning", "All fields must be filled!")
        return

    send_button.configure(state="disabled")
    progress_bar.set(0)

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)

        for idx, recipient in enumerate(recipients):
            message = MIMEMultipart("mixed")  # use mixed to allow attachments
            message["Subject"] = subject
            message["From"] = sender_email
            message["To"] = recipient

            # HTML part
            html_part = MIMEText(message_body, "html")
            message.attach(html_part)

            # Attachments
            for file_path in attachment_paths:
                try:
                    with open(file_path, "rb") as file:
                        mime_part = MIMEBase("application", "octet-stream")
                        mime_part.set_payload(file.read())
                        encoders.encode_base64(mime_part)
                        mime_part.add_header("Content-Disposition", f"attachment; filename={os.path.basename(file_path)}")
                        message.attach(mime_part)
                except Exception as e:
                    print(f"Failed to attach {file_path}: {e}")

            server.sendmail(sender_email, recipient, message.as_string())
            progress_bar.set((idx + 1) / len(recipients))

        server.quit()
        messagebox.showinfo("Success", "Emails sent successfully!")

    except smtplib.SMTPAuthenticationError:
        messagebox.showerror("Error", "Authentication failed! Check email and password.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to send emails: {e}")
    finally:
        send_button.configure(state="normal")

def threaded_send(sender_email_entry, password_entry, recipient_email, subject_entry, message_text, send_button, progress_bar):
    threading.Thread(target=send_email, args=(sender_email_entry, password_entry, recipient_email, subject_entry, message_text, send_button, progress_bar)).start()


def clear_all(sender_email_entry, password_entry, recipient_email, subject_entry, message_text, progress_bar):
    # For Entry widgets use delete(0, "end")
    sender_email_entry.delete(0, "end")
    password_entry.delete(0, "end")
    subject_entry.delete(0, "end")

    # For Textbox widgets use delete("1.0", "end")
    recipient_email.delete("1.0", "end")
    message_text.delete("1.0", "end")

    # Reset progress bar
    progress_bar.set(0)









