from flask import Blueprint, render_template, redirect, url_for, session, flash
from sqlalchemy.exc import IntegrityError
from flask_login import login_required
from ...forms.forms import DietForm, FoodForm
from ...models.models import Diet, Food, db
from ...models.cliente_model import Cliente

diet_bp = Blueprint('diet', __name__, url_prefix='/diet')

@diet_bp.route('/new', methods=['GET', 'POST'])
@login_required
def new_diet():
    diet_form = DietForm()
    food_form = FoodForm()

    if 'diet_data' in session:
        diet_form = DietForm(data=session['diet_data'])
        food_form = FoodForm(data=session['food_data'])

    if diet_form.validate_on_submit() and food_form.validate_on_submit():
        try:
            diet = Diet(
                name=diet_form.name.data,
                objective=diet_form.objective.data,
                restrictions=diet_form.restrictions.data,
                duration=diet_form.duration.data,
                cliente_id=diet_form.cliente.data.id
            )
            db.session.add(diet)
            db.session.commit()

            for food_data in food_form.food_entries.data:
                food = Food(
                    name=food_data['name'],
                    quantity=food_data['quantity'],
                    diet_id=diet.id
                )
                db.session.add(food)

            db.session.commit()

            session.pop('diet_data', None)
            session.pop('food_data', None)

            return redirect(url_for('diet.view_diet', diet_id=diet.id))

        except IntegrityError:
            db.session.rollback()
            session['diet_data'] = diet_form.data
            session['food_data'] = food_form.data
            flash("Erro ao salvar dieta e alimentos.", "error")

    return render_template('diet/form_diet.html', diet_form=diet_form, food_form=food_form)

@diet_bp.route('/all', methods=['GET'])
def view_all_diets():
    diets = Diet.query.all()
    return render_template('diet/view_diet.html', diets=diets)


