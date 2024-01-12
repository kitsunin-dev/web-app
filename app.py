from random import randint

from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

refresh = 0


@app.route("/code/?username=<username>&password=<password>")
def code(username, password):
    global refresh
    refresh += 1
    if refresh > 1:
        refresh = 0
        return redirect(url_for("survey"))

    if username == "admin" and password == "password":
        return str(randint(0, 9999)).zfill(4)
    return "Неверные данные! Повторите попытку авторизации."


@app.route("/", methods=["GET"])
def survey():
    user = request.args.get("username")
    psw = request.args.get("password")
    if user and psw:
        return redirect(url_for("code", username=user, password=psw))
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
