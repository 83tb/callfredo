#!/usr/bin/env python

import logging, logging.handlers

from twilio.rest import TwilioRestClient

ACCOUNT_SID = 'AC782ab20af29cb4bc1be863601e54f1e1'
AUTH_TOKEN = '547518f3e6116718819e8208a129f328'

# Outgoing Caller ID
# This is the dev sandbox number.
# You'll need to set up your own number with Twilio.
CALLER_ID = '6503186255';

# People you'll be messaging.
PEOPLE = {'Ola': '+16508624743',}

# Logging setup.
logger = logging.getLogger('sms')
formatter = logging.Formatter('%(levelname)s: %(asctime)s - %(message)s')
handler = logging.handlers.RotatingFileHandler('batch_sms.log',
    maxBytes=30000,
    backupCount=5)
handler.setFormatter(formatter)
logger.addHandler(handler)

# Change INFO to ERROR to stop logging success messages.
logger.setLevel(logging.INFO)

# Twilio REST API version.
API_VERSION = '2010-04-01'

# Twilio SMS resource path.
SMS_PATH = r'/%s/Accounts/%s/SMS/Messages' % (API_VERSION, ACCOUNT_SID)

# Create a Twilio REST account object.
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)


import uuid # from http://zesty.ca/python/uuid.html
import sys
import base64


def fetch_code():

    b64uid = '0000'


    uid = uuid.uuid4()
    b64uid = base64.b64encode(uid.bytes,'-_')

    code = b64uid[0:4]
    return code.upper()

def send(name, code,number):
    # Construct the SMS text.

    message = 'Hey %s, this is your callfredo verification code: %s' % (name,code)
    # Send an SMS with a POST.
    try:
        message = client.sms.messages.create(to=number, from_=CALLER_ID,
            body=message)
        logger.info('SMS sent to %s at %s' % (name, number))
    except Exception, e:
        logger.error('Failed to SMS %s. %s' % (name, e))




