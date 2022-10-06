import os
import base64

# ファイルを読み込んでBase64変換でテキストにする
#filename = "base64_input.txt"
filename = "test_pdf.pdf"
with open(filename, "br") as f: # "br"はbinaryの"b"とread-onlyの"r"が合体したもので、"b"というのが大事
    f_base64 = base64.b64encode(f.read()) # ファイルの中身を読んでbase64に変換
    str_base64 = f_base64.decode("utf-8") # そのままだとBytes型になっているので、str型に変換
print(str_base64[0:5]) # Bytes型の名残である"b'~~~'"がについていないことを先頭数文字で確認
print(type(str_base64)) # ついでにちゃんとstr型になっているかも確認
with open("base64_encoded.txt","w") as f2:
    f2.write(str_base64) #コピペ用
