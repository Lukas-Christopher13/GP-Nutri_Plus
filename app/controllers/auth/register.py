from . import auth

from flask import render_template, redirect, url_for, request

from flask_login import login_required, current_user

from sqlalchemy.exc import IntegrityError

from ...models.cliente_model import Cliente
from ...utils.register_utils import compare_passwords
from ...repository.cliente_repository import ClienteRepository
from ...repository.nutricionista_repository import NutricionistaRepository
from ...forms.auth.register_form import ClientRegisterForm, NutricionistaRegisterForm


clienteRepository = ClienteRepository()
nutricionistaRepository = NutricionistaRepository()

@auth.route("/register", methods=["GET", "POST"])
@login_required
def register():
    form = ClientRegisterForm(request.form)

    is_valid = form.validate()
    is_post = request.method == "POST"
    is_the_same_password = compare_passwords(form.password.data, form.confirm_password.data)

    if is_valid and is_post and is_the_same_password:
        try:
            nutricionista = current_user

            cliente = Cliente(
                email=form.email.data,
                full_name=form.full_name.data,
                birt_date=form.birt_date.data,
                cpf=form.cpf.data,
                country=form.country.data,
                state=form.state.data,
                city=form.city.data,
                phone_number=form.phone_number.data,
                nutricionista=nutricionista
            )
            cliente.set_password(form.password.data)

            clienteRepository.create_cliente(cliente)
            return redirect("/")
        #terminar a questão da integridade do banco!
        except IntegrityError as e:
            print(e)
            
    return render_template("auth/register.html", form=form)

@auth.route("/register-nutricionista", methods=["GET", "POST"])
@login_required
def register_nutricionista():
    form = NutricionistaRegisterForm(request.form)

    is_valid = form.validate()
    is_post = request.method == "POST"
    is_the_same_password = compare_passwords(form.password.data, form.confirm_password.data)

    if is_valid and is_post and is_the_same_password:
        try:
            nutricionistaRepository.create_cliente(form)
            return redirect("/")
        #terminar a questão da integridade do banco!
        except IntegrityError as e:
            print(e)

    return render_template("auth/nutricionista_register.html", form=form)

