import os
import random
#import pandas as pd 

#recipients.csvを作成するスクリプト

#user1~user100までのアドレスリストを作る
address_list = []
for i in range(1,100+1,1):
    address_temp = "user" + str(i) + "@example.com"
    address_list.append(address_temp)

#同様に年齢リストを作る
age_list = []
for i in range(100):
    age_list.append(random.randint(20, 70))

#gitpod上のディレクトリ関係がよくわからないので取得してみただけ
path = os.getcwd()
filepath = str(path) + "/recipients.csv"

#アドレスを一行ずつ書き込んでいく
with open(filepath,"w",encoding="utf-8") as f:
    f.write("address,age/n")
    for address,age in zip(address_list,age_list):
        f.write(address + "," + age + "\n")


#pandas.Dataframeで丸ごと中身を作ってからCSVに出す
#https://karupoimou.hatenablog.com/entry/2019/04/29/004305



