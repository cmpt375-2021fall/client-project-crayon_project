from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from socket import gethostname
 
import smtplib

def sendEmail(user_email,report_path):

    server = smtplib.SMTP('smtp.office365.com', 587)
    server.starttls()
    server.login('crayontip@outlook.com', 'Hao123123!')
    msg = MIMEMultipart()
    message = f'{"This is the report of your design from Crayon Tip"}\nSend from Hostname: {gethostname()}'
    msg['Subject'] = "quiz report"
    msg['From'] = 'crayontip@outlook.com'
    msg['To'] = user_email
    msg.attach(MIMEText(message, "plain"))
    with open(report_path, "rb") as f:
            attach = MIMEApplication(f.read(),_subtype="pdf")
    attach.add_header('Content-Disposition','attachment',filename=str(report_path))
    msg.attach(attach)
    
    try:
        server.send_message(msg)
        print("Successfully send email")
    except Exception as e:
        print(e)
        

    server.quit()
 