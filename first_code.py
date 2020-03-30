from smtplib import SMTPException
from smtplib import SMTP
import ssl

smtp_server = 'smtp.gmail.com'
port = 587
sender = 'pratimasingh160101@gmail.com'
password = input('enter ur password here:')
context = ssl.create_default_context()

try:
    server = SMTP(smtp_server, port)
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login(sender, password)
    print('it worked')

except SMTPException as e:
    print(e)
finally:
    server.quit()
