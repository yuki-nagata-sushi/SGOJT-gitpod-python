import os
import sendgrid
import base64

# MCのContactsに対して指定したRecipient（アドレス）を削除するスクリプト
# Recipientのid＝base64表現のメールアドレスであるため、それを用意する

# Step1:アドレスリストを作成
address_list = []
for i in range(1,100+1,1):
    address_list.append("user"+str(i)+"@example.com")

# Step2:作成したアドレスリストについて、中身をbase64エンコードする
# Step2-1:エンコードする関数を定義する
def encode_to_base64(val):
    val = base64.b64encode(val.encode())# encode()でbytes型に変換した後でb64変換する
    val = val.decode("utf-8") #b64encodeの返り値はbytes型なので、str型に変換する
    return val
# Step2-2:リストの全要素に同じ処理をする
map_b64 = map(encode_to_base64,address_list)# map()が全要素iterの仕事をしている
address_list_b64 = list(map_b64)# そのままではmapオブジェクトなので、list型に変換する
#以上で「削除対象アドレスのid、すなわちメルアドをbase64変換したもの」のリストが用意できた

# Step3:SendGridにリクエストを送る
sg = sendgrid.SendGridAPIClient(api_key=os.environ.get("SENDGRID_API_KEY"))
response = sg.client.contactdb.recipients.delete(request_body=address_list_b64)
print(response.status_code)
print(response.body)
