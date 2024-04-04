from . import auth

from flask import render_template, redirect, url_for, request

from sqlalchemy.exc import IntegrityError

from ...utils.register_utils import compare_passwords
from ...forms.auth.register_form import ClientRegisterForm
from ...repository.cliente_repository import ClienteRepository

clienteRepository = ClienteRepository()

@auth.route("/register", methods=["GET", "POST"])
def register():
    form = ClientRegisterForm(request.form)

    is_valid = form.validate()
    is_post = request.method == "POST"
    is_the_same_password = compare_passwords(form.password.data, form.confirm_password.data)

    if is_valid and is_post and is_the_same_password:
        try:
            clienteRepository.create_cliente(form)
            return redirect("/")
        except IntegrityError as e:
            print(e)
            
    return render_template("auth/register.html", form=form)

@auth.route("/register-nutricionista", methods=["GET", "POST"])
def register_nutricionista():
    return "registrar nutricionista"