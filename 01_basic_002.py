import os

#temp.txtの中身を読んでprintするスクリプト

path = os.getcwd()
filepath = path + "/temp.txt"
with open(filepath,"r") as f:
    s = f.read()
print(s)