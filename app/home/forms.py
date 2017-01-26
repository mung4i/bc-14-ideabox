from flask_wtf import FlaskForm
from wtforms import Form, SubmitField, TextField, validators
from wtforms.validators import DataRequired
from ..models import Users, Data

class IdeaboxForm(FlaskForm):
    title = TextField('enter title here', validators=[DataRequired()])
    description = TextField('Enter your new idea **with markdown support**',
                            validators=[DataRequired()])
    submit = SubmitField('Submit')


class IdeaboxComments(FlaskForm):
    comment = TextField('Leave a comment', validators=[DataRequired()])
    submit = SubmitField('Submit')
