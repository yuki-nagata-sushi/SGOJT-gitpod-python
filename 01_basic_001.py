import os

#temp.txtを作るスクリプト

# #gitpod上のディレクトリ関係がよくわからないので表示させてみただけ
path = os.getcwd()
print(path)

filepath = str(path) + "/temp.txt"
print(filepath)

f = open(filepath,"w",encoding="utf-8")
f.write("user1@example.com")
f.close()

#withだとclose()しなくて済むよ
# with open(filepath,"w",encoding="utf-8") as f:
#     f.write("user1@example.com")

