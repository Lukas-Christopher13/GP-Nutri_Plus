from flask import Blueprint, render_template, request, flash, redirect, url_for
from ...models.models import Activity, db
from ...forms.forms import ActivityForm
from . import activity

def calcular_calorias(intensidade, duracao):
    if intensidade.lower() == 'baixa':
        return duracao * 5
    elif intensidade.lower() == 'média':
        return duracao * 8
    elif intensidade.lower() == 'alta':
        return duracao * 12
    else:
        return duracao * 7

@activity.route('/register', methods=['GET', 'POST'])
def register_activity():
    form = ActivityForm()

    if form.validate_on_submit():
        nome_atividade = form.nome_atividade.data
        duracao = form.duracao.data
        intensidade = form.intensidade.data
        data_atividade = form.data_atividade.data
        
        calorias_queimadas = calcular_calorias(intensidade, duracao)

        activity = Activity(
            nome_atividade=nome_atividade, 
            duracao=duracao, 
            intensidade=intensidade, 
            data_atividade=data_atividade,
            calorias_queimadas=calorias_queimadas
        )
        db.session.add(activity)
        db.session.commit()

        #flash('Atividade registrada com sucesso!', 'success')
        return redirect(url_for('activity.register_activity'))

    return render_template('activity/register_activity.html', form=form)


@activity.route('/view_activities')
def view_activities():
    activities = Activity.query.all()
    return render_template('activity/view_activities.html', activities=activities)
