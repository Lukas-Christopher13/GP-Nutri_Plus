from . import cliente
from flask import render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from datetime import datetime
from ...models.consulta_model import Consulta
from ...repository.consulta_repository import ConsultaRepository
from ...services.agendar_consulta_service import ConsultaService
from ...forms.cliente.agendar_consulta_form import AgendarConsultaForm
from ...utils.notifications.remacacao_de_consulta import notificar_remaracacao_de_consulta


@cliente.route("/remarcar_consulta/<consulta_date>/<consulta_time>", methods=["GET", "POST"])
@login_required
def remarcar_consulta(consulta_date, consulta_time):
    consultaRepository = ConsultaRepository()
    consultas = consultaRepository.get_all_by_date(consulta_date)

    consulta_a_remarcar = None
    for consulta in consultas:
        if consulta.time == consulta_time:
            consulta_a_remarcar = consulta
            break

    if not consulta_a_remarcar or consulta_a_remarcar.cliente_id != current_user.id:
        flash("Consulta não encontrada ou não autorizada", "error")
        return redirect(url_for("cliente.agendar_consulta"))

    form = AgendarConsultaForm(request.form)

    if request.method == "POST" and form.validate():
        new_date = form.date.data
        new_time = form.time.data[0]

        if consultaRepository.time_already_scheduled(new_date, new_time):
            message = "Outro cliente já agendou uma consulta para esse horário"
            return render_template("cliente/remarcar_consulta.html", form=form, message=message)

        if new_date.strftime("%Y-%m-%d") == datetime.today().strftime("%Y-%m-%d"):
            message = "Você deve remarcar sua consulta com um dia de antecedência!"
            return render_template("cliente/remarcar_consulta.html", form=form, message=message)

        if datetime.today() > datetime.strptime(new_date.strftime("%Y-%m-%d"), "%Y-%m-%d"):
            message = "Essa data já passou!"
            return render_template("cliente/remarcar_consulta.html", form=form, message=message)

        
        consulta_a_remarcar.date = new_date
        consulta_a_remarcar.time = new_time
        consulta_a_remarcar.status = "Aguardando Confirmação"
        consultaRepository.update(consulta_a_remarcar)

        flash("Consulta remarcada com sucesso e aguardando confirmação!", "success")
        notificar_remaracacao_de_consulta(current_user)
        
        return redirect(url_for("cliente.agendar_consulta"))

    return render_template("cliente/remarcar_consulta.html", form=form)