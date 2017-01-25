from flask import render_template, redirect, url_for, abort, flash
from flask_login import login_required, current_user
from . import home
from forms import IdeaboxForm, IdeaboxComments
from .. import db
from ..models import Users, Data


def check_user():
    if not current_user:
        abort(403)


@home.route('/index')
@login_required
def list_ideas():
    check_user()
    ideas = Data.query.filter_by(users_email=current_user.email).all()

    return render_template('home/index.html', ideas=ideas, title="List of ideas")


@home.route('/ideabox/new', methods=['POST', 'GET'])
@login_required
def ideabox():

    check_user()
    add_data = True
    form = IdeaboxForm()

    if form.validate_on_submit():
        data = Data(
            title=form.title.data,
            description =form.description.data, users_email=current_user.email)
        try:
            db.session.add(data)
            db.session.commit()
            flash('Success!')
        #exception string to debug if commit fails
        except Exception, e:
            db.session.rollback()
            print str(e)
            flash('Idea already exists')
        return redirect(url_for('home.list_ideas'))
    return render_template('home/ideabox.html', action="Add", add_data=add_data, form=form, title="Add idea")

@home.route('/ideabox/edit/',methods=['POST', 'GET'])
@login_required
def edit_ideabox():
    check_user()
    add_data = False
    data = Data.query.filter_by(users_email=current_user.email).first()
    print data
    form = IdeaboxForm(obj=data)
    print form
    if form.validate_on_submit():
        data.title = form.title.data
        data.description = form.description.data
        db.session.commit()
        flash('Edit successful')
        return redirect(url_for('home.list_ideas'))

    form.title.data = data.title
    form.description.data = data.description

    print "Form 2nd", form
    return render_template('home/ideabox.html', action="Edit", add_data=add_data, form=form, data=data, title="Edit idea")


@home.route('/ideabox/delete/<int:id>', methods=['POST', 'GET'])
@login_required
def deleteIdea(id):
    check_user()
    ideas = Data.query.get_or_404(id)
    db.session.delete(ideas)
    db.session.commit()
    flash('Delete successful')

    return redirect(url_for('home.list_ideas'))
    return render_template(title="Delete idea")
