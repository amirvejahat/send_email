import smtplib
from builtins import print
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.encoders import encode_base64

GMAIL_USERNAME = 'YOUR GMAIL ADDRESS'
GMAIL_PASSWORD = 'YOUR GMAIL PASSWORD'


class Gmail():

    def __init__(self,username,password):
        self.message = MIMEMultipart()
        self.username = username
        self.password = password
        self.server = 'smtp.gmail.com'
        self.port = 587
        connection = smtplib.SMTP(self.server,self.port)
        connection.ehlo()
        connection.starttls()
        connection.login(self.username,self.password)
        print('Sent Email!')
        self.connection = connection

    def attachment(self,file):
        part = MIMEBase('application', "octet-stream")
        part.set_payload(open(file, "rb").read())
        encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="{}"'.format(file))
        self.message.attach(part)

    def send_message(self, to, subject, content):

        self.message["From"] = self.username
        self.message["to"] = to
        self.message["Subject"] = subject
        self.message.attach(MIMEText(content,'plain'))
        self.message = self.message.as_string()
        self.connection.sendmail(self.username,to,self.message)
        self.connection.close()


to = input("TO : ")
subject = input("Subject : ")
print("Message : ")
msg = ""
while True:
    try:
        msg += input()
    except EOFError:
        break
    if msg == "":
        break


gm = Gmail(GMAIL_USERNAME,GMAIL_PASSWORD)
gm.attachment("/home/csr/Pictures/test.jpg")
gm.send_message(to,subject,msg)
