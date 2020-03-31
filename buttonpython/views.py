from django.shortcuts import render
import os
import imghdr
import smtplib
from email.message import EmailMessage
import csv


def button(request):
    return render(request, 'home.html')


def output(request):
    # import sendEmail
    print('sent')
    clean_data = []
    receivers_email = []
    i = int

    with open('emails.csv', encoding='utf8') as csv_file:
        contacts = csv.DictReader(csv_file)
        for contact in contacts:
            email = contact['Email']
            if email:
                info = {'Name': contact['Name'], 'Email': contact['Email']}
                if info not in clean_data:
                    clean_data.append(info)
    for em in clean_data:
        receivers_email.append(em['Email'])
    # for i, e in enumerate(clean_data):
    # print(i, e)
    # sendEmail.send_email(e[1])
    # for receiver in receivers_email:
    #    print(receiver)

    MY_EMAIL = os.environ.get('EMAIL_USER')

    # receivers_email = ['vedantagrawal5109@gmail.com', 'vidita7agrawal@gmail.com', 'angelagarwal63@gmail.com',
    # 'prasoonjain006@gmail.com',
    # 'pratimasingh160101@gmail.com']

    def send_email(to):
        message = EmailMessage()
        message['subject'] = "COVID-19 Volunteers"
        message['from'] = MY_EMAIL
        message['to'] = to
        message.set_content('for assistance ')
        html_message = open('first_temp.html').read()
        message.add_alternative(html_message, subtype='html')

        with open('Screenshot (66).png', 'rb') as attach_file:
            image_name = attach_file.name
            image_type = imghdr.what(attach_file.name)
            image_data = attach_file.read()

        message.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(MY_EMAIL, os.environ['EMAIL_PASS'])
            smtp.send_message(message)

    for receiver in receivers_email:
        send_email(receiver)
        i = 23
    if i ==23:
        data = 'sent succesfully!!'
    print(data)

    return render(request, 'home.html', {'data':data})

