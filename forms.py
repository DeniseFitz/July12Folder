from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms import BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),
                           Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(),
                                                 EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    logname = StringField('Username',
                          validators=[DataRequired(),
                                      Length(min=2, max=20)])
    logpass = PasswordField('Password', validators=[DataRequired()])
    logint = IntegerField('Some number', validators=[DataRequired()])
    logbool = BooleanField('ckit')
    submit = SubmitField('Log In')
