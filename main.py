from flask import Flask, render_template
import requests
from post import Post

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
    #return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for post in post_objects:
        if post.id == index:
            requested_post = post
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)
