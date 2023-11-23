from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,IntegerField,TextAreaField,SelectField
from wtforms.validators import DataRequired, Length, Regexp, Optional, NumberRange


class Proposal_Form(FlaskForm):
    
    subject = TextAreaField('Tema', validators=[DataRequired(), Length(min=5, max=100)])
   
    description = TextAreaField('Descripción', validators=[DataRequired(), Length(min=5, max=600)])
    proposal_type = SelectField('Opciones', choices=[('1', 'CHARLA'), ('2', 'ACTIVIDAD'), ('3', 'STAND')])

    submit = SubmitField('Crear Propuesta')

