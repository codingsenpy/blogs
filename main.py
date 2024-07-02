from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    res=requests.get("https://api.npoint.io/e847ed20ca107fdb6237")
    blogs=res.json()
    return render_template("index.html",blogs=blogs)

@app.route('/post/<int:idn>')
def post(idn):
    res = requests.get("https://api.npoint.io/e847ed20ca107fdb6237")
    blogs = res.json()
    return render_template("post.html",allblogs=blogs,idno=idn)

@app.route('/blog/<n>')
def blog(n):
    response=requests.get("https://api.npoint.io/e847ed20ca107fdb6237")
    allp=response.json()
    return render_template("blog.html",posts=allp)

if __name__ == "__main__":
    app.run(debug=True)


