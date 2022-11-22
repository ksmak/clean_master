from flask import Flask, render_template

from settings import *

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html", menu=menu, contacts=contacts, whatsapp=whatsapp)

if __name__ == "__app__":
    app.run(host='localhost', port=5000, debug=True)