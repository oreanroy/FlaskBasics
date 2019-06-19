from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author': 'Corey Scahfer',
        'title': 'First blog',
        'content': "the first blog",
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'blog 2',
        'content': "second blog",
        'date_posted': 'April 21, 2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == "__main__":
    app.run(debug=True)

