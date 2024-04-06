from ..ext.db import db
from ..models.cliente_model import Cliente
from ..forms.auth.register_form import ClientRegisterForm

class ClienteRepository:
    def create_cliente(self, form: ClientRegisterForm):
        cliente = Cliente(
            email = form.email.data,
            full_name = form.full_name.data,
            birt_date = form.birt_date.data,
            cpf = form.cpf.data,
            country = form.country.data,
            state = form.state.data,
            city = form.city.data,
        )
        cliente.set_password(form.password.data)

        
        db.session.add(cliente)
        db.session.commit()
