
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, FloatField, DateField
from wtforms.validators import DataRequired

class DietForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    objective = TextAreaField('Objective')
    restrictions = TextAreaField('Restrictions')
    duration = IntegerField('Duration (days)', validators=[DataRequired()])

class FoodForm(FlaskForm):
    name = StringField('Food Name', validators=[DataRequired()])
    quantity = FloatField('Quantity (grams)', validators=[DataRequired()])


class ActivityForm(FlaskForm):
    nome_atividade = StringField('Nome da Atividade', validators=[DataRequired()])
    duracao = IntegerField('Duração (minutos)', validators=[DataRequired()])
    intensidade = StringField('Intensidade', validators=[DataRequired()])
    data_atividade = DateField('Data da Atividade', validators=[DataRequired()])

