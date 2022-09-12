import os
import sendgrid
from collections import defaultdict
import json

# 複数の宛先へ個別内容メールをwithout-helperで一斉送信するスクリプト
sg  = sendgrid.SendGridAPIClient(api_key=os.environ.get("SENDGRID_API_KEY"))

# まずはメール内容をdict型（≒JSON形式）で用意する
# step1: 50件の宛先を生成する
to_list = []
for i in range(1,49+1,1):
    to_list.append("user" + str(i) + "@" + os.environ.get("SG_TEST_DOMAIN"))
to_list.append(os.environ.get("MY_EMAIL_ADDRESS"))

# step2: personalizationにて参照する受信者名を生成する
name_list = []
for i in range(1,49+1,1):
    name_list.append("name" + str(i))
name_list.append("sushi_man")

# step3: personalizationsに入れる宛先リストのlistを用意する
# dict型は本来同じ名前のkeyに別の要素を代入できない（上書きされる）が、リストにして代入することはできる（リスト「1つ」になるため）
temp_list = [] # リストの初期化
for itr_address,itr_name in zip(to_list,name_list): # 宛先アドレスと名前を順番に入れていく
    temp_list.append(
        {
        "to": [{"email": itr_address}],
        "substitutions": 
        {
            "%name%": itr_name
        },
        "subject": "Hello %name% !"
        }
    )# 上記構造は通常通りの形式を踏襲する。これが1セットになってリストに追加されていく。
添付ファイル出資
# step4: メール内容を用意する
data_dict = defaultdict(dict) # dict型の初期化（宣言）。defaultdictを使うとkeyの存在有無を確かめずに済む
data_dict["personalizations"] = temp_list
data_dict["from"] = {"email": os.environ.get("MY_EMAIL_ADDRESS_FROM")}
data_dict["content"] = [
    {
        "type": "text/plain",
        "value": "test body for %name%"
    }
]

# print(temp)
# print(data_dict)
print(json.dumps(data_dict,indent=4)) # 見やすい形に変換してチェックしてみる

# 実際にメールを送信する
response = sg.client.mail.send.post(request_body=data_dict) # request_bodyにdictを突っ込むのはやはり違和感があるな...
print(response.status_code)
print(response.body)
print(response.headers)