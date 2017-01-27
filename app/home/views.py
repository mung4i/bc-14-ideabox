from flask import render_template, redirect, url_for, abort, flash
from flask_login import login_required, current_user
from . import home
from forms import IdeaboxForm, IdeaboxComments
from .. import db
from ..models import Users, Data, Comments

def check_user():
    if not current_user:
        abort(403)

@home.route('/index', methods=['POST', 'GET'])
@home.route('/')
@login_required
def list_ideas():
    #List all ideas function which calls all ideas posted by users and renders to the users' indexpage
    check_user()
    ideas = Data.query.filter_by(users_email=current_user.email).all()
        # return redirect(url_for('home.list_ideas'))
    #functionality added to load comments
    form=IdeaboxComments()
    if form.validate_on_submit():
        comment = Comments(comment=form.comment.data, users_email=current_user.email)
        db.session.add(comment)
        db.session.commit()

    comments= Comments.query.filter_by(comment_id=id).all()
    return render_template('home/index.html', ideas=ideas, form=form, comments=comments, title="List of ideas")


@home.route('/ideabox/new', methods=['POST', 'GET'])
@login_required
def ideabox():
    #Form to create new idea built from this method
    #if user is authenticated a WTForm is rendered from this route
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
    #edit function called, title cannot be changed
    #user set description updates the db using an SQLAlchemy
    #update method.
    check_user()
    add_data = False
    form = IdeaboxForm()
    form_title=form.title.data
    if form.validate_on_submit():
        data = Data(title = form.title.data, description = form.description.data, users_email=current_user)
        query = Data.query.filter_by(title=data.title).update(dict(description=form.description.data))
        db.session.commit()
        flash('Edit successful')
        return redirect(url_for('home.list_ideas'))
    return render_template('home/ideabox.html', action="Edit", add_data=add_data, form=form, title="Edit idea", placeholder=form_title)

@home.route('/ideabox/comments',methods=['POST','GET'])
@login_required
def comment_ideabox():
    #function not working gives a 200 but does not post to db
    form = IdeaboxComments()
    if form.validate_on_submit():
        comment = Comments(comment=form.comment.data, users_email=current_user.email)
        db.session.add(comment)
        db.session.commit()
        flash('comment has been published')
        return redirect(url_for('home.comment_ideabox'))
    else:
        flash('Comment publish failed', error)
    return render_template('home/ideabox.html', action="Comment", query=query, form=form, title="Comment")
