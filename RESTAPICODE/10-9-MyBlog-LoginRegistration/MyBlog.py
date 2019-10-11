from flask import Flask, render_template, url_for, flash, redirect
from flask_json import FlaskJSON, JsonError, json_response, as_json
from forms import RegistrationForm,LoginForm
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import json
from pathlib import Path

import os


app = Flask(__name__)
app.config['SECRET_KEY'] = '40147847450f6b27952430f017e97620'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

json = FlaskJSON(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

posts = [
    {
        'author': 'Rajesh Gupta',
        'title' : 'The First Blog',
        'id' : 'P0001',
        'content' : 'This is the first post content and will keep adding.This is the first post content and will keep adding.This is the first post content and will keep adding,This is the first post content and will keep adding.......',
        'date_posted' : 'Oct 6,2019'
    },
    {
            'author': 'Rajesh Gupta',
            'title' : 'The Second Blog',
            'id' : 'P0002',
            'content' : 'This is the Second post content and will keep adding.......',
            'date_posted' : 'Oct 7,2019'
        }
]


@app.route('/')
@app.route('/home')
def home():
    #return render_template('C:\\Users\\Rajesh Kumar Gupta\\Documents\\GitProjects\\PythonCodes\\virtualEnv\\sandbox\\templates\\home.html')
    cur_user= User.query.first().username
    print(cur_user)
    return render_template('home.html',title='Home',posts=posts,cur_user=cur_user)

@app.route('/about')
def about():
    return render_template('about.html',title='About')

@app.route('/Post')
def post():
    return render_template('Post.html',title='Post')

@app.route('/PostDetails/<string:id>', methods=['GET','POST'])
def PostDetails(id):
    print (id)
    redirect_Page='Post'+id+'.html'
    return render_template(redirect_Page,title='Post')

@app.route('/login', methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html',title='Login',form=form)

@app.route('/register', methods=['GET','POST'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html',title='Register',form=form)

@app.route('/contact')
def contact():
    return render_template('UnderConstruction.html',title='contact')

@app.route('/document')
def document():
    return render_template('Test.html',title='Multitenancy')

@app.route('/bye')
def say_bye():
  return 'Bye from Server'

@app.route('/get_time')
def get_time():
    now = datetime.utcnow()
    return json_response(time=now)

@app.route('/get_value')
@as_json
def get_value():
    return dict(value=12)

if __name__ == '__main__':
    app.run(debug=True)
