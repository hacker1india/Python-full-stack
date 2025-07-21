from flask_wtf import FlaskForm 
from wtforms import StringField, TextAreaField, SubmitField 
from wtforms.validators import DataRequired, length 

class FeedbackForm(FlaskForm):
    name = StringField('Name',validators=(DataRequired(),length(min=2,max=50)))
    feedback = TextAreaField('Feedback',validators=(DataRequired(),length(min=5)))
    submit = SubmitField('submit')