from . import cliente

from flask import render_template, redirect, url_for, request
from flask_login import login_required, current_user

from ...models.consulta_model import Consulta
from ...repository.consulta_repository import ConsultaRepository
from ...services.agendar_consulta_service import CalendarConsulta
from ...forms.cliente.agendar_consulta_form import AgendarConsultaForm


CALENDAR_NUM_DAYS = 5

@cliente.route("/agendar_consulta", methods=["GET", "POST"])
@login_required
def agendar_consulta():
    form = AgendarConsultaForm(request.form)
    consultaRepository = ConsultaRepository()

    calendars = CalendarConsulta.get_calendar(CALENDAR_NUM_DAYS, consultaRepository)

    if not (request.method == "POST" and form.validate()):
        return render_template("cliente/agendar_consulta.html", form=form, calendars=calendars)
    
    date = form.date.data
    time = form.time.data[0]
    
    if consultaRepository.time_already_scheduled(date, time):
        message = "Outro cliente já agendou uma consulta para esse horário"
        return render_template("cliente/agendar_consulta.html", form=form, calendars=calendars, message=message)

    consulta = Consulta(
        date=form.date.data,
        time=time,
        status="Agendado",
        cliente_id=current_user.id
    )

    consultaRepository.insert(consulta)

    return redirect(url_for("cliente.agendar_consulta"))
    