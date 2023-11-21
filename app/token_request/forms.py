from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,IntegerField,TextAreaField
from wtforms.validators import DataRequired, Length, Regexp, Optional, NumberRange


class Token_Request_Form(FlaskForm):
    num_token = IntegerField('Número de tokens (1 token = 1 propuesta)', validators=[DataRequired(),NumberRange(min=1,max=3)])
    description = TextAreaField('Descripción', validators=[DataRequired(), Length(min=5, max=600)])
   
    submit = SubmitField('Pedir token')