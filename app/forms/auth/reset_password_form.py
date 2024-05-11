from wtforms import Form, EmailField, PasswordField, validators

class ResetPasswordForm(Form):
    email = EmailField("Email")