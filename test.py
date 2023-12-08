from flask import Flask, render_template, request
#import requests

app = Flask(__name__)

@app.route('/')
def home():
    #return render_template("index.html", posts=post_objects)
    return render_template("index_test.html")

@app.route('/login', methods=["POST"])
def receive_data():
    #return "TEST RECEIVED!!"
    if request.method == 'POST':
        return f"<h1> Name: {request.form['name']}, password: {request.form['password']}</h1>"

if __name__ == "__main__":
    app.run(debug=True)
