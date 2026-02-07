import smtplib
from email.message import EmailMessage

def send_mail(sender, app_password, receiver, subject, body):
    msg = EmailMessage()

    msg ["From"] = sender
    msg ["To"] = receiver
    msg["Subject"] = subject 

    msg.set_content(body)

    smtp = smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)

    smtp.login(sender, app_password)

    smtp.send_message(msg)

    smtp.quit()


def main():
    sender_email = "sudarshanahire12@gmail.com"

    app_password = "XXXX XXXX XXXX XXXX"

    receiver_email = "sudarshanahire4347@gmail.com"

    subject = "Test Mail from Python Script"

    body = """Jay Ganesh.
        This is a test email sent using python Marvellous Python.
        Regards,
        Marvellous Infosystems"""

    # Marvellous_send_mail(sender_email, app_password, receiver_email, subject, body):
    send_mail(sender_email, app_password, receiver_email, subject, body)


    print("Marvellous Mail Sent Successfully")

if __name__ == "__main__":
    main()


