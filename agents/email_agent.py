import smtplib
from email.mime.text import MIMEText
import streamlit as st

SENDER_EMAIL = "pranjulshukla481@gmail.com"  # TODO: Replace this
APP_PASSWORD = "sifv vfnn gibq wswm"     # TODO: Replace this

def send_confirmation_email(name, item, quantity, recipient):
    subject = "Order Confirmation"
    body = f"Hello {name},\n\nYour order for {quantity} x {item} has been received and is being processed.\n\nThank you!"

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = SENDER_EMAIL
    msg['To'] = recipient

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(SENDER_EMAIL, APP_PASSWORD)
            smtp.send_message(msg)
        st.success("Confirmation email sent successfully.")
    except Exception as e:
        st.error(f"Failed to send email: {e}")