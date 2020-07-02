# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACbf49fe14378f7451d0665173575f06fb'
auth_token = 'e6cb096c1094ade8bf334a9823406cbb'
client = Client(account_sid, auth_token)

message = client.messages .create(body="Hi Rohit, This is a message from your PC, Keep Hustling.",from_='+15088124097',to='+918787898226')

print(message)
