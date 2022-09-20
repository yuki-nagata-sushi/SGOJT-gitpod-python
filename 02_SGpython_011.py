import os
from sendgrid import SendGridAPIClient # これしか使わないので限定しても問題ない

sg = SendGridAPIClient(os.environ.get("SENDGRID_API_KEY"))

response = sg.client.contactdb.recipients.get()

print(response.status_code)
print(response.body)
