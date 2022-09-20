import sendgrid
import os
import json

# bounceリストをGETしてくるスクリプト

sg = sendgrid.SendGridAPIClient(api_key=os.environ.get("SENDGRID_API_KEY"))

response = sg.client.suppression.bounces.get()
print(response)
# print(response.body)
# print(response.headers)

# # インデントをつけて見やすくしたいと欲張ったが駄目だった名残
# b_ResponseBody = response.body
# str_ResponseBody = b_ResponseBody.decode("utf-8")
# print(type(str_ResponseBody))

# l = eval(str_ResponseBody)
# print(l)
# print(json.dumps(str_ResponseBody,indent=4))