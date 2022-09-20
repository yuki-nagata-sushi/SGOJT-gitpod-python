import os
from sendgrid import SendGridAPIClient

# Contacts list に登録されているリストの一覧をGETするスクリプト

sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
response = sg.client.contactdb.lists.get()

print(response.status_code)
print(response.body)