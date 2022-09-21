from flask import Flask, request 
from json import dumps 

# flaskを用いてSendGridがPOSTしてくるEventWebhookを受け取るアプリ（？）

# gitpod上のPORTSタブ（TERMINALの横辺り）でポートやその{Public,Private}の管理が簡単にでき、
# そこで"Make Public"するだけで外部からアクセスできる。
# だが恐らくngrokのようなローカルトンネルとは違って本当に「公開」されてしまっている。

app = Flask(__name__) # おまじない

@app.route("/endpoint",methods=["POST"]) # https://{ip}/endpointに"POST"してくる場合Display_jsonを実行する
def Display_json():
    json_list = request.get_json() # https://tedboy.github.io/flask/generated/generated/flask.Request.get_json.html
    print(type(json_list[1])) # json_listはdictのlistであることがわかる
    for data in json_list:
        dumped = dumps(data,indent=4) # インデントを4つ下げて見やすくする
        print(dumped)
    return "" # 戻り値を指定しないと不都合があるようだ。https://www.self-study-blog.com/dokugaku/python-funstion-return-none-multiple/

if __name__ == "__main__":# こっちはpythonのおまじない。自身を呼び出したときにここを実行することを指定するとかなんとか（cf.ライブラリ）
    app.run(debug=True)