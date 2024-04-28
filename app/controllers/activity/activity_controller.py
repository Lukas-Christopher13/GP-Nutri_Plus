from flask import Blueprint, render_template, request, flash, redirect, url_for
from ...models.models import Activity, db
from ...forms.forms import ActivityForm
from . import activity


@activity.route('/register', methods=['GET', 'POST'])
def register_activity():
    form = ActivityForm()

    if form.validate_on_submit():
        nome_atividade = form.nome_atividade.data
        duracao = form.duracao.data
        intensidade = form.intensidade.data
        data_atividade = form.data_atividade.data
        
        # Salvar os dados da atividade no banco de dados
        activity = Activity(nome_atividade=nome_atividade, duracao=duracao, intensidade=intensidade, data_atividade=data_atividade)
        db.session.add(activity)
        db.session.commit()

        flash('Atividade registrada com sucesso!', 'success')
        return redirect(url_for('activity.register_activity'))

    return render_template('activity/register_activity.html', form=form)

