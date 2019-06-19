from flask import Flask, render_template, url_for, flash, redirect
from datetime import datetime
from forms import RegistraionForm, LoginForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY']='5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpeg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return "user {}, {}, {}".format({self.username}, {self.email}, {self.image_file})
        # "user {}, {}, {}".format({self.username}, {self.email}, {self.image_file})
        # "User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


    def __repr__(self):
        return "Post {}, {}".format({self.title}, {self.date_posted})
        # "Post {}, {}".format({self.title}, {self.date_posted})
        # f"Post('{self.title}', '{self.date_posted}')"

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

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistraionForm()
    if form.validate_on_submit():
        flash('Account cretaed for user, {} !'.format({form.username.data}), 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == '123':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Your login was nor succesful', 'danger')
            return redirect(url_for('login'))
    return render_template('login.html', title='Login', form=form)



if __name__ == "__main__":
    app.run(debug=True)

