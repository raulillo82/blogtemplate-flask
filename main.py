from flask import Flask, render_template, request
import requests
from post import Post
from auth import APIKEY_ALPHAVANTAGE, APIKEY_NEWSAPI, bot_chatID,  bot_token

app = Flask(__name__)

blog_url = "https://api.npoint.io/79af83afe03463a29f67"
response = requests.get(blog_url)
all_posts = response.json()
post_objects = [Post(post["id"],
                     post["title"],
                     post["subtitle"],
                     post["body"],
                     post["date"],
                     post["author"],
                     post["image"],
                     ) for post in all_posts]

@app.route('/')
def home():
    return render_template("index.html", posts=post_objects)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == 'POST':
        data = request.form
        if send_telegram_message(data["name"], data["email"], data["phone"],
                                 data["message"]):
            text = "Sucessfully sent message"
        else:
            text = "Error when sending the message, please try again!"
    elif request.method == 'GET':
        text = "Contact me"
    return render_template("contact.html", text=text)

@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for post in post_objects:
        if post.id == index:
            requested_post = post
    return render_template("post.html", post=requested_post)

def send_telegram_message(name, email, phone, message):
    msg = f"Subject: Contact form from {name}\n"
    msg += f"Email: {email}\n"
    msg += f"Phone: {phone}\n"
    msg += f"Message: {message}\n\n"
    params = {
            "chat_id": bot_chatID,
            "text": msg,
            "parse_mode": "MARKDOWN",
            }
    url = "https://api.telegram.org/bot" + bot_token + "/sendMessage"
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    app.run(debug=True)
