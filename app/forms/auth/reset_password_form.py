from wtforms import Form, EmailField, SubmitField
from wtforms.validators import DataRequired

class ResetPasswordForm(Form):
    email = EmailField("Email")
    submit = SubmitField(label="Reset Password", validators=[DataRequired()])