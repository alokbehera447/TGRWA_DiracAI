from django.conf import settings
import os
import random

try:
    from twilio.rest import Client
except ModuleNotFoundError:
    Client = None



class MessageHandler:
    phone_number = None
    otp = None
    def __init__(self, phone_number, otp)->None:
        self.phone_number = phone_number
        self.otp = otp
 
    def send_otp_on_phone(self):
        if Client is None:
            raise ModuleNotFoundError("twilio is not installed")
        client = Client(settings.ACCOUNT_SID, settings.AUTH_TOKEN)

        message = client.messages.create(
                              body=f'Your otp {self.otp}',
                              from_='+19894398139',
                              to=self.phone_number
                          )        















