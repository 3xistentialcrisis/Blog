from flask import render_template,redirect,url_for
from app.main import main
from app.request import get_quotes

@main.route('/')
def index():
    quotes = get_quotes()
    print(quotes)
    return render_template('index.html')

@main.route('/profile')
def profile():
    return render_template('profile/profile.html')