from wtforms import Form, DateField, SelectMultipleField
from wtforms.validators import DataRequired

#adicionar Campo motivo
class AgendarConsultaForm(Form):
    choices=[
        ('opcao1', 'Opção 1'),
        ('opcao2', 'Opção 2'),
        ('opcao3', 'Opção 3')
    ]
    #validator para excluir sabado e domingo
    date = DateField("Data da Consulta", [DataRequired()])
    time = SelectMultipleField("Horário da Consutla", choices=choices, validators=[DataRequired()])

