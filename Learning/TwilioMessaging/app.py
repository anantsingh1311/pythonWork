import os
import sys

from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

if not account_sid or not auth_token:
    sys.exit(
        "Missing credentials. Set TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN\n"
        "(copy .env.example to .env and fill it in, then use `pipenv run python app.py`)."
    )

from_number = os.environ.get("TWILIO_FROM", "+17372508034")
to_number = os.environ.get("TWILIO_TO", "+918800852155")

client = Client(account_sid, auth_token)

try:
    message = client.messages.create(
        to=to_number,
        from_=from_number,
        body="My First message",
    )
except TwilioRestException as e:
    print(f"Twilio rejected the message (HTTP {e.status}, error {e.code})")
    print(f"  {e.msg}")
    if e.details:
        print(f"  details: {e.details}")
    print(f"  see: {e.uri}")
    sys.exit(1)

print(f"queued: {message.sid}")
print(f"status: {message.status}")
