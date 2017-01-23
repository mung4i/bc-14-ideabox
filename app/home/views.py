#app/home/views.py

from flask import render_template

from flask_login import login_required

from . import home

@home.route('/')
def homepage():
    '''
    Renders homepage on the index route
    '''

    return render_template('home/index.html', title="Welcome")

@home.route('/ideabox')
@login_required
def ideabox():
    '''
    Renders the ideabox template on the ideabox route
    '''

    return render_template('home/ideabox.html', title="IdeaBox")
