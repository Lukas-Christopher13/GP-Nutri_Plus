
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, FloatField, DateField, FieldList, FormField
from wtforms.validators import DataRequired

class DietForm(FlaskForm):
    name = StringField('Nome', validators=[DataRequired()])
    objective = TextAreaField('Objetivo')
    restrictions = TextAreaField('Restrições')
    duration = IntegerField('Duração (dias)', validators=[DataRequired()])

class FoodForm(FlaskForm):
    name = StringField('Nome da Comida', validators=[DataRequired()])
    quantity = FloatField('Quantidade (gramas)', validators=[DataRequired()])

class MultipleFoodForm(FlaskForm):
    food_entries = FieldList(FormField(FoodForm), min_entries=1) 


class ActivityForm(FlaskForm):
    nome_atividade = StringField('Nome da Atividade', validators=[DataRequired()])
    duracao = IntegerField('Duração (minutos)', validators=[DataRequired()])
    intensidade = StringField('Intensidade', validators=[DataRequired()])
    data_atividade = DateField('Data da Atividade', validators=[DataRequired()])

