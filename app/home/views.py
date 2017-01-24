from flask import render_template, redirect, url_for, abort, flash
from flask_login import login_required, current_user
from . import home
from forms import IdeaboxForm, IdeaboxComments
from .. import db
from ..models import Data


def check_user():
    if not current_user:
        abort(403)


@home.route('/index')
@login_required
def homepage():
    return render_template('home/index.html',title="Welcome")


@home.route('/ideabox', methods=['POST', 'GET'])
@login_required
def ideabox():

    check_user()

    add_data = True

    form = IdeaboxForm()

    if form.validate_on_submit():
        data = Data(
            name=form.name.data,
            description =form.description.data)
        try:
            db.session.add(data)
            db.session.commit()
            flash('Success!')
        except:
            flash('Idea already exists')
        return redirect(url_for('home.homepage'))
    return render_template('home/ideabox.html', action="Add", add_data=add_data, form=form, title="Add idea")

def deleteIdea():
    check_user()
    data = Data.query.all()
    db.session.delete(data)
    db.session.commit()

    flash('Delete successful')

    return redirect(url_for('home.ideabox'))
