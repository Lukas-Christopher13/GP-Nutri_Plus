from ..ext.db import db
from ..models.nuticionista_model import Nutricionista
from ..forms.auth.register_form import NutricionistaRegisterForm

class NutricionistaRepository:
     def create_cliente(self, form: NutricionistaRegisterForm):
        nutricionista = Nutricionista(
            email = form.email.data,
            full_name = form.full_name.data,
            birt_date = form.birt_date.data,
            cnpj = form.cnpj.data,
        )
        nutricionista.set_password(form.password.data)

        db.session.add(nutricionista)
        db.session.commit()
    