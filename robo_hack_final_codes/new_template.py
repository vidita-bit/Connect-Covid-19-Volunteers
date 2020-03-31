import os  # for user id and password calling as set in enviornment variables
import smtplib  # for setting server connection
from email.message import EmailMessage  # for sending message after connection is send
import csv  # for reading data from excel file

clean_data = []  # list created for clearing data as the scraped data may have duplicacy
receivers_email = []  # list of email id taken from excel file

with open('emails.csv', encoding='utf8') as csv_file:
    contacts = csv.DictReader(csv_file)  # sorting the data of students email id
    for contact in contacts:
        email = contact['Email']
        if email:
            info = {'Name': contact['Name'], 'Email': contact['Email']}
            if info not in clean_data:
                clean_data.append(info)
for em in clean_data:
    receivers_email.append(em['Email'])

MY_EMAIL = os.environ.get('EMAIL_USER')


def send_email(to):  # email syntax
    message = EmailMessage()
    message['subject'] = "COVID-19 Volunteers"
    message['from'] = MY_EMAIL
    message['to'] = to
    message.set_content('for assistance ')
    html_message = open('final_html.html').read()
    message.add_alternative(html_message, subtype='html')

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(MY_EMAIL, os.environ['EMAIL_PASS'])
        smtp.send_message(message)


for receiver in receivers_email:                            # sending application form to all students in the excel list
    send_email(receiver)
