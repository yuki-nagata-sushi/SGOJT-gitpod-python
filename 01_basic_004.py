import requests

#URLからサイトのHTMLを取ってくるスクリプト

r = requests.request(method="GET", url="https://www.python.jp")
#r2 = requests.get(url="https://www.python.jp") #こんな書き方もあるよ。こっちの方が何をしているかわかりやすい。

print(r) #これだとステータス200が返る事しかわからない
print(r.text) #こうするとちゃんとHTMLが見える

with open("r.txt", mode="w") as f:
    f.write(r.text) #txtに書き出しても、日本語の文字化けは直らない。terminalの問題ではなさそう。

