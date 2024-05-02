from flask import Blueprint, render_template, redirect, url_for, session, flash
from sqlalchemy.exc import IntegrityError
from ...forms.forms import DietForm, FoodForm
from ...models.models import Diet, Food, db

diet_bp = Blueprint('diet', __name__, url_prefix='/diet')

@diet_bp.route('/new', methods=['GET', 'POST'])
def new_diet():
    diet_form = DietForm()
    food_form = FoodForm()

    if 'diet_data' in session:
        diet_form = DietForm(data=session['diet_data'])
        food_form = FoodForm(data=session['food_data'])

    if diet_form.validate_on_submit() and food_form.validate_on_submit():
        try:
            diet = Diet(name=diet_form.name.data,
                        objective=diet_form.objective.data,
                        restrictions=diet_form.restrictions.data,
                        duration=diet_form.duration.data)
            db.session.add(diet)
            db.session.commit()

            
            for food_data in food_form.food_entries.data:
                food = Food(name=food_data['name'],
                            quantity=food_data['quantity'],
                            diet_id=diet.id)
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

@diet_bp.route('/<int:diet_id>')
def view_diet(diet_id):
    diet = Diet.query.get_or_404(diet_id)
    foods = Food.query.filter_by(diet_id=diet_id).all()
    return render_template('diet/view_diet.html', diet=diet, foods=foods)
