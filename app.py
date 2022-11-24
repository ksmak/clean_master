from flask import Flask, render_template

from settings import *

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html", 
        menu=menu, 
        contacts=contacts, 
        whatsapp=whatsapp,
        clean_list=clean_list
    )

@app.route("/send_order", methods=['POST'])
def send_order():
    return render_template("success.html")

if __name__ == "__app__":
    app.run(host='localhost', port=5000, debug=True)