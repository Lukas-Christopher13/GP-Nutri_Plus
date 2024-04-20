from . import auth

from flask import render_template, redirect, request

from flask_login import login_required, current_user

from ...models.nuticionista_model import Nutricionista
from ...models.cliente_model import Cliente
from ...utils.register_utils import compare_passwords
from ...repository.cliente_repository import ClienteRepository
from ...repository.nutricionista_repository import NutricionistaRepository
from ...forms.auth.register_form import ClientRegisterForm, NutricionistaRegisterForm

from ...services.auth.errors import EmailAlreadyRegistredError
from ...services.auth.register_service import NutricionistaRegisterService


@auth.route("/register", methods=["GET", "POST"])
@login_required
def register():
    form = ClientRegisterForm(request.form)
    clienteRepository = ClienteRepository()

    if not (request.method == "POST" and form.validate()):
        return render_template("auth/register.html", form=form)
    
    if form.password.data != form.confirm_password.data:
        message = "Passwords diferentes!"
        return render_template("auth/register.html", form=form, message=message)
    
    if clienteRepository.email_already_exists(form.email.data):
        message = "Esse email já foi cadastrado"
        return render_template("auth/register.html", form=form, message=message)

    nutricionista = current_user

    cliente = Cliente(
        email=form.email.data,
        full_name=form.full_name.data,
        birt_date=form.birt_date.data,
        cpf=form.cpf.data,
        country=form.country.data,
        state=form.state.data,
        city=form.city.data,
        nutricionista=nutricionista
    )
    cliente.set_password(form.password.data)

    clienteRepository.insert(cliente)
    return redirect("/")
   

@auth.route("/register-nutricionista", methods=["GET", "POST"])
#@login_required
def register_nutricionista():
    form = NutricionistaRegisterForm(request.form)
    nutricionistaRepository = NutricionistaRepository()
    nutricionistaRegisterService = NutricionistaRegisterService(nutricionistaRepository)

    if not (request.method == "POST" and form.validate()):
        return render_template("auth/nutricionista_register.html", form=form)

    if form.password.data != form.confirm_password.data:
        message = "Passwords diferentes!"
        return render_template("auth/nutricionista_register.html", form=form, message=message)
        
    nutricionista = Nutricionista(
        email = form.email.data,
        full_name = form.full_name.data,
        birt_date = form.birt_date.data,
        cnpj = form.cnpj.data
    )
    
    nutricionista.set_password(form.password.data)

    try:
        nutricionistaRegisterService.register(nutricionista)
        return redirect("/")

    except EmailAlreadyRegistredError as e:
        message = "Esse email já foi cadastrado"
        return render_template("auth/nutricionista_register.html", form=form, message=message)    