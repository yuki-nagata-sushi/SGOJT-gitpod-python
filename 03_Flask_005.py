# リクエストが来るとこのコード全体が実行される
#from flask import response # このスタイルだとflask.requestとrequestsが紛らわしいのでやめる
import flask
import os
import requests
from json import dumps

slack_incoming_webhook = os.environ.get("SLACK_INCOMING_WEBHOOK")

app = flask.Flask(__name__)
@app.route("/", methods=["POST"])
def main():
    print("from", flask.request.form["from"])
    print("To", flask.request.form["to"])
    print("Subject", flask.request.form["subject"])
    print("Body", flask.request.form["text"])
    return ""

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0", port=int(os.environ.get("PORT", 3000)))
    # app.run(debug=True)


