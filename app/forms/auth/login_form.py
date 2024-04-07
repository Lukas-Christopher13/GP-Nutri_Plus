from wtforms import Form, EmailField, PasswordField, validators

class LoginForm(Form):
    email = EmailField("Email do usuário")
    password = PasswordField("Password do usuário")
