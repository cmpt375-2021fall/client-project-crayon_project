# import os
# from django.core.mail import send_mail

# os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

# if __name__ == '__main__':   

#     # send_mail(
#     #     '来自喵喵喵的测试邮件',
#     #     '?????',
#     #     'panyuyuyu@outlook.com',
#     #     ['winter0416@hotmail.com'],
#     # )

import smtplib

def sendEmail():

    server = smtplib.SMTP('smtp.office365.com', 587)
    server.starttls()
    server.login('crayontip@outlook.com', 'Hao123123!')
    message = 'Subject: {}\n\n{}'.format("love", "i love panyu")
    try:
        server.sendmail('crayontip@outlook.com', 'winter0416@hotmail.com', message)
        print("Successfully sent email")
    except:
        print('An error occurred when trying to send an email')
        

    server.quit()

sendEmail()