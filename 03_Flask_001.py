import flask

app = flask.Flask(__name__)

@app.route("/") # "http://{ip}/" （つまりトップ）にアクセスしてきた場合にhello()を実行する
def hello():
    return "Hello,World!"

if __name__ == "__main__":
    app.run(debug=True)
