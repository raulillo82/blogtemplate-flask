from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(blog_url)
all_posts = response.json()
post_objects = [Post(post["id"],
                     post["title"],
                     post["subtitle"],
                     post["body"],
                     ) for post in all_posts]

@app.route('/')
def home():
    return render_template("index.html", posts=post_objects)

@app.route('/post/<int:index>')
def show_post(index):
    for post in post_objects:
        if post.id == index:
            requested_post = post
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)
