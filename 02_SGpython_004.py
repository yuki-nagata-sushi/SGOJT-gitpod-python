import os
import sendgrid
import json

# 複数の宛先へ個別内容メールをwithout helperで一斉送信するスクリプト

# まずはメール内容をdict型（≒JSON形式）で用意する
# step1 宛先を生成する
to_list = []
for i in range(1,49+1,1):
    to_list.append("user"+str(i)+"")