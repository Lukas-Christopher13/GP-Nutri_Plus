from wtforms import Form, EmailField, SubmitField, PasswordField
from wtforms.validators import DataRequired

class ResetPasswordForm(Form):
    email = EmailField("Email")
    submit = SubmitField(label="Reset Password", validators=[DataRequired()])

class SetNewPasswordForm(Form):
    password = PasswordField("password", validators=[DataRequired()])
    confirm_password = PasswordField("confirme password", validators=[DataRequired()])

    submit = SubmitField(label="Reset Password", validators=[DataRequired()])
    