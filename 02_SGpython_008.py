import sendgrid
import os
from python_http_client.exceptions import HTTPError

# https://github.com/sendgrid/sendgrid-python/blob/main/examples/contactdb/contactdb.py#:~:text=%23-,Delete,-Multiple%20lists%20%23
sg = sendgrid.SendGridAPIClient(api_key=os.environ.get("SENDGRID_API_KEY"))

temp_list = []
for i in range(1,50+1,1):
    temp_list.append("list"+str(i))

try:
    response = sg.client.contactdb.lists.delete(request_body=temp_list)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except HTTPError as e:
    print(e.to_dict)

