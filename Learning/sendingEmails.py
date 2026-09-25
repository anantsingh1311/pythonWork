from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
import smtplib 
from string import Template

tempelate = Template(Path("template.html").read_text())

message = MIMEMultipart()

message["from"] = "Anant Singh"
message["to"] = "anantsingh1311@gmail.com"
message["subject"] = "This is a test"

# body = tempelate.substitute({"name":"Anant"})
# or
body = tempelate.substitute(name="Anant")
message.attach(MIMEText(body,"html"))
# message.attach(MIMEText("Body"))
# message.attach(MIMEImage(Path("image.png").read_bytes()))

with smtplib.SMTP(host="smtp.gmail.com",port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("anantwork15@gmail.com","xjrc xgfm abfv eixf")
    smtp.send_message(message)
    print("Sent..")
