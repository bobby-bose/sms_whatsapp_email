import pywhatkit
import wmi as wmi
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.
import socket
from twilio.rest import Client
import wmi

def send_maill(request):
    send_mail(
        'Subject here',
        'Here is the message.',
        settings.EMAIL_HOST_USER,
        ['bobbykboseoffice@gmail.com'],

    )
    return HttpResponse('Mail sent successfully')


def send_whatsapp(request):
    number = "Enter the number Here"
    message = "Hello Hacker"
    pywhatkit.sendwhatmsg_instantly(number, message, 10)
    return HttpResponse('Whatsapp sent successfully')

def make_call(request):


    # Find your Account SID and Auth Token at twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    account_sid = 'ACb2e5c320c3f02b2d7f1b973d305827fb'
    auth_token = '20ebfc31c4762143596a4369548f9f8f'
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body='This is the ship that made the Kessel Run in fourteen parsecs?',
        from_='+12183047576',
        to='+917012085349'
    )

    print(message.sid)
    return HttpResponse('Call sent successfully')


def get_computer_details(request):

    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print(f"Hostname: {hostname}")
    print(f"IP Address: {ip_address}")

    return HttpResponse('Computer details')