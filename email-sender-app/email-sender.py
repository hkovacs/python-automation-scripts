# Requires a Google Account with 2-Step Verification (2FA) enabled
# Set values in .env
# GMAIL_USER = "your.email@gmail.com"
# GMAIL_APP_PASSWORD = "your-16-char-app-password"

from email.message import EmailMessage
import os
from pathlib import Path
import smtplib
from dotenv import load_dotenv

# Explicitly point to the .env file in the same folder as emailsender.py
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)


def send_email(recipient: str, subject: str, body: str) -> None:
    # Load credentials safely from environment variables
    sender_email = os.environ.get("GMAIL_USER")
    app_password = os.environ.get("GMAIL_APP_PASSWORD")

    if not sender_email or not app_password:
        raise ValueError("Missing GMAIL_USER or GMAIL_APP_PASSWORD environment variables.")

    # Construct a properly formatted email
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = recipient
    msg.set_content(body)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, app_password)
            server.send_message(msg)
        print("Email sent successfully!")
    except smtplib.SMTPAuthenticationError:
        print("Failed to authenticate. Check your email and Google App Password.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    to_email = input("Enter the recipient's email:\n").strip()
    mail_subject = input("Enter the subject:\n").strip()
    mail_content = input("Enter the content for the mail:\n")

    send_email(to_email, mail_subject, mail_content)
