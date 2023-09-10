import smtplib
import ssl
import imghdr
from email.message import EmailMessage

SENDER = "nika.patatishvili@gmail.com"
PASSWORD = ""


def send_mail(image_path):
    email_message = EmailMessage()
    email_message["Subject"] = "New customer showed up"
    email_message.set_content("Hey, we just saw a new customer!")

    with open(image_path, 'rb') as f:
        content = f.read()

    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, "nikoloz.patatishvili@gau.edu.ge", email_message.as_string())
    gmail.quit()


if __name__ == "__main__":
    send_mail("images/capture13.png")
