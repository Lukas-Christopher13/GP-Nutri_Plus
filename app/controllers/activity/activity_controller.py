from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import current_user, login_required
from ...models.models import Activity, db
from ...forms.forms import ActivityForm
from . import activity
import matplotlib.pyplot as plt
import os


def calcular_calorias(intensidade, duracao):
    if intensidade.lower() == 'baixa':
        return duracao * 5
    elif intensidade.lower() == 'média':
        return duracao * 8
    elif intensidade.lower() == 'alta':
        return duracao * 12
    else:
        return duracao * 7



def gerar_grafico_evolucao(activities):
    datas = [activity.data_atividade for activity in activities]
    calorias_queimadas = [activity.calorias_queimadas for activity in activities]
    durações = [activity.duracao for activity in activities]

    plt.figure(figsize=(10, 5))
    plt.plot(datas, calorias_queimadas, label='Calorias Queimadas', marker='o')
    plt.plot(datas, durações, label='Duração', marker='s')
    plt.xlabel('Data')
    plt.ylabel('Valores')
    plt.title('Evolução das Atividades')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()

    if not os.path.exists('static'):
        os.makedirs('static')

    plt_path = 'app/static/evolucao_atividades.png'
    plt.savefig(plt_path)
    plt.close()

    return plt_path

@activity.route('/register', methods=['GET', 'POST'])
@login_required
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
            calorias_queimadas=calorias_queimadas,
            cliente_id=current_user.id
        )
        db.session.add(activity)
        db.session.commit()

        
        return redirect(url_for('home.cliente_home_page'))

    return render_template('activity/register_activity.html', form=form)


@activity.route('/view_activities')
@login_required
def view_activities():
    activities = Activity.query.all()
    plt = gerar_grafico_evolucao(activities)
    return render_template('activity/view_activities.html', activities=activities, plt=plt)
    
    