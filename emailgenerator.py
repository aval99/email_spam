import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
count = 0
b = True
f = open("email.txt")
while b:
    c = f.readline()
    subject = "An email with attachment from Python"
    body = "This is an email with attachment sent from Python"
    sender_email = "science.fiesta@lac.edu.np"
    receiver_email = c
    password = "LACFIESTA"


# Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Add body to email
    message.attach(MIMEText(body, "plain"))



    # Add attachment to message and convert message to string

    text = message.as_string()

    # Log in to server using secure context and send email
    # Log in to server using secure context and send email
    if c == "":
            b = False
    else:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, text) # Log in to server using secure context and send email
            count = count + 1
            print("Mail sent to:", count)

