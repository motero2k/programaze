from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,IntegerField,TextAreaField,BooleanField
from wtforms.validators import DataRequired, Length, Regexp, Optional, NumberRange


class Vote_Form(FlaskForm):
    
    description = TextAreaField('Descripción', validators=[DataRequired(), Length(min=5, max=600)])
    decision = BooleanField('Decisión')
    submit = SubmitField('Votar')
   