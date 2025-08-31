from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class RegistrationForm(FlaskForm):
    name =StringField("Full Name", validators=[DataRequired(message="Have you entered your username")])
    email =StringField("Email", validators=[DataRequired("Have you  entered your email"), Email("Have you entered your valid email")])
    password= PasswordField("Password", validators=[DataRequired("Have you entered password"), Length(9)])
    submit = SubmitField("Register")
