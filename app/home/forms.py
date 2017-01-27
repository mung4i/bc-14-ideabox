'''
Forms class that serves WTF forms to app templates.
'''
from flask_wtf import FlaskForm
from wtforms import Form, SubmitField, TextField, validators
from wtforms.validators import DataRequired
from ..models import Users, Data

class IdeaboxForm(FlaskForm):
    title = TextField('Title:', validators=[DataRequired()])
    description = TextField('Description:',
                            validators=[DataRequired()])
    submit = SubmitField('Submit')


class IdeaboxComments(FlaskForm):
    comment = TextField('Leave a comment', validators=[DataRequired()])
    submit = SubmitField('Submit')
