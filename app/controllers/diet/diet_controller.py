from flask import Blueprint, render_template, redirect, url_for
#from app.forms.forms import DietForm, FoodForm
from ...forms.forms import DietForm, FoodForm
#from app.models.models import Diet, Food, db
from ...models.models import Diet, Food, db

diet_bp = Blueprint('diet', __name__, url_prefix='/diet')

@diet_bp.route('/new', methods=['GET', 'POST'])
def new_diet():
    diet_form = DietForm()
    food_form = FoodForm()

    if diet_form.validate_on_submit() and food_form.validate_on_submit():
        diet = Diet(name=diet_form.name.data,
                    objective=diet_form.objective.data,
                    restrictions=diet_form.restrictions.data,
                    duration=diet_form.duration.data)
        db.session.add(diet)
        db.session.commit()

        food = Food(name=food_form.name.data,
                    quantity=food_form.quantity.data,
                    diet_id=diet.id)
        db.session.add(food)
        db.session.commit()

        return redirect(url_for('diet.view_diet', diet_id=diet.id))

    return render_template('diet/form_diet.html', diet_form=diet_form, food_form=food_form)

@diet_bp.route('/<int:diet_id>')
def view_diet(diet_id):
    diet = Diet.query.get_or_404(diet_id)
    foods = Food.query.filter_by(diet_id=diet_id).all()
    return render_template('diet/view_diet.html', diet=diet, foods=foods)
