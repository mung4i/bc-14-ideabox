from flask import render_template

from flask_login import login_required

from . import home


@home.route('/index')
def homepage():
    return render_template('home/index.html', title="Welcome")


@home.route('/ideabox')
@login_required
def ideabox():
    return render_template('home/ideabox.html', title="IdeaBox")
