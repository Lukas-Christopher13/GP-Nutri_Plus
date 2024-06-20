from flask import Blueprint, render_template, redirect, request, url_for
from flask_login import login_required
from ...forms.forms import DietForm, FoodForm
from ...models.models import Diet, Food, db
from . import diet

@diet.route('/new', methods=['GET', 'POST'])
@login_required
def new_diet():
    diet_form = DietForm()
    food_form = FoodForm()

    if diet_form.validate_on_submit():
        #obter dados do formulário de dieta
        name = diet_form.name.data
        objective = diet_form.objective.data
        restrictions = diet_form.restrictions.data
        duration = diet_form.duration.data
        cliente_id = diet_form.cliente.data.id

        diet = Diet(
            name=name,
            objective=objective,
            restrictions=restrictions,
            duration=duration,
            cliente_id=cliente_id
        )
        db.session.add(diet)
        db.session.commit()

        food_names = request.form.getlist('food_name')
        food_quantities = request.form.getlist('food_quantity')

        for food_name, food_quantity in zip(food_names, food_quantities):
            if food_name and food_quantity:
                food = Food(
                    name=food_name,
                    quantity=food_quantity,
                    diet_id=diet.id  
                )
                db.session.add(food)

        db.session.commit()

        return redirect(url_for('diet.view_all_diets'))

    return render_template('diet/form_diet.html', diet_form=diet_form, food_form=food_form)


@diet.route('/all', methods=['GET'])
@login_required
def view_all_diets():
    diets = Diet.query.all()
    return render_template('diet/view_diet.html', diets=diets)
