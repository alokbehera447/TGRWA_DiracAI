from django.conf import settings
import os
from twilio.rest import Client
import random



class MessageHandler:
    phone_number = None
    otp = None
    def __init__(self, phone_number, otp)->None:
        self.phone_number = phone_number
        self.otp = otp
 
    def send_otp_on_phone(self):
        client = Client(settings.ACCOUNT_SID, settings.AUTH_TOKEN)

        message = client.messages.create(
                              body=f'Your otp {self.otp}',
                              from_='+19894398139',
                              to=self.phone_number
                          )        















