import os
import json
import requests

# requestsライブラリを利用してメール送信リクエストをPOSTするスクリプト

# 環境変数から各種値を取ってくる
api_key = os.environ.get("SENDGRID_API_KEY")
to_address = os.environ.get("MY_EMAIL_ADDRESS")
from_address = os.environ.get("MY_EMAIL_ADDRESS_FROM")

# POSTの中身を用意していく

# まずはHeadersを用意する。こっちは辞書typeでOK
# Authorizationが無い場合は401Unauthorizedが、Content-Typeが無い場合は415UnsupportedMediaTypeが返ってくる。
header_py = {"Authorization":"Bearer "+api_key, "Content-Type":"application/json"} 

# 次に実際のBodyを用意する。まずは普通の辞書で書いて、その後ライブラリを利用してjsonに変換する
payload = {
    "personalizations":[
        {
            "to":[{"email":to_address}],
            "subject":"Hello,world!"
        }
    ],
    "from":{"email":from_address},
    "content":[
        {
            "type":"text/plain",
            "value":"testbody"
        }
    ]
}

endpoint = "https://api.sendgrid.com/v3/mail/send"
json_data = json.dumps(payload) # ここで辞書→json変換している。そうしないと400Badrequestが返ってくる

# 実際にPOSTする
r = requests.post(url=endpoint, headers=header_py, data=json_data)
print(r)