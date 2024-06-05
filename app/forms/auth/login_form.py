from wtforms import Form, EmailField, PasswordField, validators

class LoginForm(Form):
    email = EmailField("Email do usuário")
    password = PasswordField("Password do usuário")

class LoginADMForm(Form):
    email = EmailField("Email do usuário")
    password = PasswordField("Password do usuário", [validators.Length(min=8, max=16)])

class RegisterDeviceForm(Form):
    email = EmailField("Email do Nutricionista", [validators.Length(min=8, max=16)])
