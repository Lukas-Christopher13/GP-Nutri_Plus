
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, FloatField
from wtforms.validators import DataRequired

class DietForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    objective = TextAreaField('Objective')
    restrictions = TextAreaField('Restrictions')
    duration = IntegerField('Duration (days)', validators=[DataRequired()])

class FoodForm(FlaskForm):
    name = StringField('Food Name', validators=[DataRequired()])
    quantity = FloatField('Quantity (grams)', validators=[DataRequired()])

