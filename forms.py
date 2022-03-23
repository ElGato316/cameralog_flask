from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateTimeField, SelectField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    login = SubmitField('Login')

class CreateUserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    active = BooleanField('Active')
    supervisor = BooleanField('Supervisor')
    role = SelectField('Role', choices=[('sgt', 'Sergeant'), ('lt', 'Lieutenant'), ('des', 'DES')])

class CreateTrainingDate(FlaskForm):
    date = DateTimeField('Class Date and Time', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    comments = StringField('Comments', validators=[DataRequired()])

class CreateOfficerForm(FlaskForm):
    badge = StringField('Badge', validators=[DataRequired()])
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    rank = StringField('Rank', validators=[DataRequired()])

class CreateLocationForm(FlaskForm):
    location = StringField('Location', validators=[DataRequired()])

class CreateReasonForm(FlaskForm):
    reason = StringField('Reason', validators=[DataRequired()])