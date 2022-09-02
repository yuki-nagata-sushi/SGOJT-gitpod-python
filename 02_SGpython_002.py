import sendgrid
import os

# helpersを使わないコードでSGのAPIにリクエストをPOSTするスクリプト

sg = sendgrid.SendGridAPIClient(api_key=os.environ.get("SENDGRID_API_KEY"))
data = {
    "personalizations": [
        {
            "to": [{"email": os.environ.get("MY_EMAIL_ADDRESS")}],
            "subject": "Hello python without helper"
        }
    ],
    "from": {"email": os.environ.get("MY_EMAIL_ADDRESS_FROM")},
    "content": [
        {
            "type": "text/plain",
            "value": "test Body without helper"
        }
    ]
}
print(type(data)) #jsonではなくdictであることに注目

response = sg.client.mail.send.post(request_body=data)
# ここで特に指定していないが、defaultでContent-Typeが"application/json"になっている
# https://github.com/sendgrid/sendgrid-python/blob/main/sendgrid/base_interface.py#:~:text=.useragent%2C-,%22Accept%22%3A%20%27application/json%27,-%7D
print(response.status_code)
print(response.body)
print(response.headers)