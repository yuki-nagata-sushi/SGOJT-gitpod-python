import os
import sendgrid
from sendgrid.helpers.mail import *

# helpersを使ったコードでSGのAPIにリクエストをPOSTするスクリプト

# 淡々と穴埋めするだけ
sg = sendgrid.SendGridAPIClient(api_key=os.environ.get("SENDGRID_API_KEY"))
from_email = Email(os.environ.get("MY_EMAIL_ADDRESS_FROM"))
to_email = To(os.environ.get("MY_EMAIL_ADDRESS"))
subject = "Hello SendGrid python helper"
content = Content("text/plain", "test Body python helper")
mail = Mail(from_email, to_email, subject, content)
response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)