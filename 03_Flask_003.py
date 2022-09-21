import os,requests
import flask
from json import dumps

slack_incoming_webhook = os.environ.get("SLACK_INCOMING_WEBHOOK")

app = flask.Flask(__name__)

@app.route("/", methods=["POST"])
def main():
    data_list = flask.request.get_json()
    
    slackblock_list = []
    for data in data_list:
        dumped = dumps(data,indent=2)
        event_name = data["event"]

        slackblock_list.append(
            {
                "type": "section",
                "text": {"type": "mrkdwn","text": f"*{event_name}*```{dumped}```"}
            }
        )

    headers = {"Content-Type":"application/json"}
    slack_json = dumps({"blocks":slackblock_list})
    requests.post(slack_incoming_webhook, headers=headers, data=slack_json)
    
    return ""

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0", port=int(os.environ.get("PORT", 3000)))
    # app.run(debug=True)