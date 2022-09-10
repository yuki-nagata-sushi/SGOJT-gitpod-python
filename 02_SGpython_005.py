import sendgrid
import os
import json

sg = sendgrid.SendGridAPIClient(api_key=os.environ.get("SENDGRID_API_KEY"))

response = sg.client.suppression.bounces.get()
print(response)
# print(response.body)
# print(response.headers)
b_ResponseBody = response.body
str_ResponseBody = b_ResponseBody.decode("utf-8")
print(type(str_ResponseBody))

l = eval(str_ResponseBody)
print(l)
# print(json.dumps(str_ResponseBody,indent=4))