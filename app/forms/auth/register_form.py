from wtforms import Form, StringField, EmailField, DateField, PasswordField, validators

class ClientRegisterForm(Form):
    email = EmailField("Email")
    full_name = StringField("Nome", [validators.Length(min=8, max=60)])
    birt_date = DateField("Data de Nascimento")
    cpf = StringField("CPF", [validators.Length(11)])
    country = StringField("Pais", [validators.Length(min=2, max=30)])
    state = StringField("Estado", [validators.Length(min=2, max=30)])
    city = StringField("Cidade", [validators.Length(min=2, max=30)])
    password = PasswordField("Password", [validators.Length(min=8, max=16)])
    confirm_password = PasswordField("Confirme o seu Password", [validators.Length(min=8, max=16)])


class NutricionistaRegisterForm(Form):
    email = EmailField("Email")
    full_name = StringField("Nome", [validators.Length(min=8, max=60)])
    birt_date = DateField("Data de Nascimento")
    cnpj = StringField("CPF", [validators.Length(11)])
    password = PasswordField("Password", [validators.Length(min=8, max=16)])
    confirm_password = PasswordField("Confirme o seu Password", [validators.Length(min=8, max=16)])