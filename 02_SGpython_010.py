import sendgrid
import os

# リストidを直書きで指定してContacts listsから削除するスクリプト

sg = sendgrid.SendGridAPIClient(api_key=os.environ.get("SENDGRID_API_KEY"))

# 削除したい
data = []
for i in range(20182123,20182173+1,1):#2018~~というのが事前にcontactdb.lists.get()で取得して手動で確認したid番号
    data.append(i)

response = sg.client.contactdb.lists.delete(request_body=data)
print(response.status_code)
print(response.body)