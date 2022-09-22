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
    data = []
    data.append(
        {
            "from": flask.request.form["from"], 
            "To": flask.request.form["to"],
            "Subject": flask.request.form["subject"], 
            "Body": flask.request.form["text"]
        }
    )
    
    dumped = dumps(data,indent=2)

    slack_block_list = []
    slack_block_list.append(
        {
            "type": "section",
            "text": {"type": "mrkdwn","text": f"*inbound mail notification!*```{dumped}```"}
        }
    )

    headers = {"Content-Type": "application/json"}
    slack_json = dumps({"blocks": slack_block_list})
    requests.post(slack_incoming_webhook, headers=headers, data=slack_json)
    return ""

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0", port=int(os.environ.get("PORT", 3000)))
    # app.run(debug=True)


