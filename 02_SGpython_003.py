import sendgrid
import os
import base64
from python_http_client.exceptions import HTTPError

# PDFを添付してwithout-helperでメール送信するスクリプト

# まずPDFを読み込んでBase64変換でテキストにする
with open("test_pdf.pdf", "br") as f: # "br"はbinaryの"b"とread-onlyの"r"が合体したもので、"b"というのが大事
    base64_testpdf = base64.b64encode(f.read()) # pdfの中身を読んでbase64に変換
    str_base64_testpdf = base64_testpdf.decode("utf-8") # そのままだとBytes型になっているので、str型に変換
print(str_base64_testpdf[0:5]) # Bytes型の名残である"b'~~~'"がについていないことを先頭数文字で確認
print(type(str_base64_testpdf)) # ついでにちゃんとstr型になっているかも確認

# メールを作成していく(02_SGpython_002.pyを参照)
sg = sendgrid.SendGridAPIClient(api_key=os.environ.get("SENDGRID_API_KEY"))
data = {
    "personalizations": [
        {
            "to": [{"email": os.environ.get("MY_EMAIL_ADDRESS")}],
            "subject": "Hello python pdf without-helper"
        }
    ],
    "from": {"email": os.environ.get("MY_EMAIL_ADDRESS_FROM")},
    "content": [
        {
            "type": "text/plain", # 添付ファイルがattachmentじゃなくてinlineだとどうなるんだろう？
            "value": "test Body pdf without-hepler"
        }
    ],
    "attachments":[ # ここが新しく追加された添付ファイル用のコード
        {
            "content": str_base64_testpdf,
            "disposition": "attachment",
            "filename": "test.pdf",
            "name": "test",
            "type": "pdf"
        }
    ]
}

try:
    response = sg.client.mail.send.post(request_body=data)
    print(response.status_code)
except HTTPError as e: # この部分はtryの方で例外が出たときに実行される
    print(e.to_dict) # エラーの詳細がprintされる便利ライブラリを利用した