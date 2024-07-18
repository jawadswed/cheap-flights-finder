import os
from twilio.rest import Client
import smtplib
from dotenv import load_dotenv

load_dotenv()


class NotificationManager:

    def __init__(self):
        self.client = Client(os.environ['TWILIO_SID'], os.environ["TWILIO_AUTH_TOKEN"])
        self.whatsapp_number = os.environ["TWILIO_WHATSAPP_NUMBER"]
        self.verified_number = os.environ["TWILIO_VERIFIED_NUMBER"]
        self.virtual_number = os.environ["TWILIO_VIRTUAL_NUMBER"]

        self._my_email = os.environ["MY_EMAIL"]
        self._my_password = os.environ["PASSWORD"]
        self.smtp_address = os.environ["SMTP_ADDRESS"]

    def send_sms(self, message_body):
        message = self.client.messages.create(
            from_=self.virtual_number,
            body=message_body,
            to=self.virtual_number
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_whatsapp(self, message_body):
        message = self.client.messages.create(
            from_=f'whatsapp:{self.whatsapp_number}',
            body=message_body,
            to=f'whatsapp:{self.verified_number}'
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_emails(self, emails_list, message_body):
        with smtplib.SMTP(self.smtp_address) as connection:
            connection.starttls()
            connection.login(self._my_email, self._my_password)
            for email in emails_list:
                connection.sendmail(
                    from_addr=self._my_email,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message_body}".encode('utf-8')
                )
