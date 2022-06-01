import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, To

my_email_address = os.environ.get("MY_EMAIL_ADDRESS")
to_1 = my_email_address.replace("@", "+1@")
to_2 = my_email_address.replace("@", "+2@")
address_list - [to_1,to_2]

name_list = ["Alice", "Bob"]
color_list = ["RED", "GREEN"]

to_emails = []
for addree,name, color in zip(address_list, name_list, color_list):
    to = To(
        email=address,
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

sendgrid_client = SendGridAPIClient(os.environ.get("SENDGRID_API_KEY"))
response = sendgrid_client.send(message)
print(response.status_code)
print(response.body)