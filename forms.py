from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

class CreateUserForm(FlaskForm):
    username = StringField('Username', validators=[DateRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Create')