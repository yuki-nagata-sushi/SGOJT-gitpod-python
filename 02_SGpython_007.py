import sendgrid
import os 

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

# step2-n:リクエストを送りまくる
for listname in temp_list:
    data = {
        "name": listname
    }
    response = sg.client.contactdb.lists.post(request_body=data)
    print(response.status_code)
    # print(response.body)
    # print(response.headers)
print("Complete POST")