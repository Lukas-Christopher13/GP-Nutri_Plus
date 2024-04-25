from wtforms import Form, DateField, SelectMultipleField, StringField, IntegerField
from wtforms.validators import DataRequired

#adicionar Campo motivo
class AgendarConsultaForm(Form):
    choices=[
        ('7:00', '7:00'),
        ('8:00', '8:00'),
        ('9:00', '9:00'),
        ('10:00', '10:00'),
        ('11:00', '11:00'),
        ('13:00', '13:00'),
        ('14:00', '14:00'),
        ('15:00', '15:00'),
        ('16:00', '16:00'),
    ]
    #validator para excluir sabado e domingo
    date = DateField("Data da Consulta", [DataRequired()])
    time = SelectMultipleField("Horário da Consutla", choices=choices, validators=[DataRequired()])

class FilterAgendarConsultaForm(Form):
    date = DateField("Data")
    register_number = IntegerField("Quantidade de datas")


