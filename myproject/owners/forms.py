from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):

    name = StringField()
    pup_id = IntegerField()
    submit = SubmitField('Add Owner')
