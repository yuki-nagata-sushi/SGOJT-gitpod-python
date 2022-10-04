import sendgrid
import os
import base64
from python_http_client.exceptions import HTTPError

# unsubscribe group 挙動確認のスクリプト

# メールを作成していく(02_SGpython_002.pyを参照)
sg = sendgrid.SendGridAPIClient(api_key=os.environ.get("SENDGRID_API_KEY"))
data = {
    "personalizations": [
        {
            "to": [{"email": os.environ.get("MY_EMAIL_ADDRESS")}],
            "subject": "Hello python without-helper"
        }
    ],
    "from": {"email": os.environ.get("MY_EMAIL_ADDRESS_FROM")},
    "content": [
        {
            "type": "text/html", # 添付ファイルがattachmentじゃなくてinlineだとどうなるんだろう？
            "value": "<a href=<%asm_preferences_raw_url%>>配信停止を管理する</a><br />test Body\nこのメールをどうにかする：<%asm_preferences_raw_url%>"
        }
    ],
    "asm": {
        "group_id": 27001
    }
}

try:
    response = sg.client.mail.send.post(request_body=data)
    print(response.status_code)
except HTTPError as e: # この部分はtryの方で例外が出たときに実行される
    print(e.to_dict) # エラーの詳細がprintされる便利ライブラリを利用した