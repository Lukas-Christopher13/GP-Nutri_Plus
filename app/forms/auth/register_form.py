from wtforms import Form, StringField, EmailField, DateField, PasswordField, validators
from wtforms.validators import DataRequired

class ClientRegisterForm(Form):
    email = EmailField("Email", [DataRequired()])
    full_name = StringField("Nome", [DataRequired(), validators.Length(min=8, max=60)])
    birt_date = DateField("Data de Nascimento")
    cpf = StringField("CPF", [DataRequired(), validators.Length(11)])
    country = StringField("Pais", [DataRequired(), validators.Length(min=2, max=30)])
    state = StringField("Estado", [DataRequired(), validators.Length(min=2, max=30)])
    city = StringField("Cidade", [DataRequired(), validators.Length(min=2, max=30)])
    password = PasswordField("Password", [DataRequired(), validators.Length(min=8, max=16)])
    confirm_password = PasswordField("Confirme o seu Password", [DataRequired(), validators.Length(min=8, max=16)])


class NutricionistaRegisterForm(Form):
    email = EmailField("Email", [DataRequired()])
    full_name = StringField("Nome", [DataRequired(), validators.Length(min=8, max=60)])
    birt_date = DateField("Data de Nascimento")
    cnpj = StringField("CPF", [DataRequired(), validators.Length(11)])
    password = PasswordField("Password", [DataRequired(), validators.Length(min=8, max=16)])
    confirm_password = PasswordField("Confirme o seu Password", [DataRequired(), validators.Length(min=8, max=16)])