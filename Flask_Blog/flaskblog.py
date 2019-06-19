from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistraionForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY']='5791628bb0b13ce0c676dfde280ba245'

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

