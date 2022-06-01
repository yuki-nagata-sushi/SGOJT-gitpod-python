import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, To

name_list = ["Alice", "Bob"]
color_list = ["RED", "GREEN"]

to_emails = []
for name, color in zip(name_list, color_list):
    to = To(
        email="to@example.com",
        name=name,
        substitutions={"-name-":name, "-color-":color}
        )
    to_emails.append(to)

message = Mail(
    from_email=("from@example.com", "Carol"),
    to_emails=to_emails,
    subject="Hello,-name-!",
    plain_text_content="Your lucky color is -color-!",
    is_multiple=True
    )

sendgrid_client = SendGridAPIClient("SG.abcd")
response = sendgrid_client.send(message)
print(response.status_code)
print(response.body)