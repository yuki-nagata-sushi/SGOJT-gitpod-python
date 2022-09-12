import sendgrid
import os 
from collections import defaultdict
from python_http_client.exceptions import HTTPError

# 「contactlistに複数のリストを作成するスクリプト」のダメな例

sg = sendgrid.SendGridAPIClient(os.environ.get("SENDGRID_API_KEY"))

# 参考までに現存するcontactlistの一覧を取得してみる
# response_get = sg.client.contactdb.lists.get()
# print(response_get.status_code)
# print(response_get.body)
# print(response_get.headers)

# step1:contactlistに追加するリスト名のlistを作る
temp_list = []
for i in range(1,50+1,1):
    temp_list.append("list"+str(i))

print(temp_list)
input("Push to continue")

# step2:APIに送るデータを作る
data = defaultdict(dict) #defaultdictで空のdictを初期化して生成
data["name"] = temp_list #"name"というkeyにstep1で作ったlistをあてる

# step3:リクエストを送る
try:
    response = sg.client.contactdb.lists.post(request_body=data)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except HTTPError as e: # この部分はtryの方で例外が出たときに実行される
    print(e.to_dict)
    # {'errors': [{'message': 'List name is invalid'}]}
    #　上記のエラーが出る。おそらく"name"にあてるデータは文字列のみで、listは対応していない。