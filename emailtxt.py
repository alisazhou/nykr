import smtplib, os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

MY_EMAIL = "alisa.zwy@gmail.com"
ARTICLE_DIR = "/articles"


def get_subject(fileName):
    seg, withSuffix = fileName.split('_')
    titleList = withSuffix[:-4].split('-')
    titleStr = ' '.join(titleList)
    subject = seg + ': ' + titleStr
    return subject
    

def get_content(fileName):
    f = open(fileName)
    content = f.read()
    f.close()
    return content

    
def compose_email(fileName):
    msg = MIMEMultipart()
    msg['Subject'] = get_subject(fileName)
    body = get_content(fileName)
    msg.attach(MIMEText(body, 'plain', errors='ignore'))
    return msg


def batch_send(artDir):
    msg = MIMEMultipart()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(MY_EMAIL, input("... sesame?"))
    for f in os.listdir(artDir):
        msg = compose_email(f)
        server.sendmail(MY_EMAIL, MY_EMAIL, msg.as_string())
    server.quit()