from typing import Dict

from sqlalchemy.exc import IntegrityError

from .errors import EmailAlreadyRegistredError

from ...models.nuticionista_model import Nutricionista
from ...repository.nutricionista_repository import NutricionistaRepository


class NutricionistaRegisterService:
    def __init__(self, nutricionistaRepositry: NutricionistaRepository) -> None:
        self.nutricionistaRepository = nutricionistaRepositry

    def register(self, nutricionista: Nutricionista):
        try:
            self.nutricionistaRepository.insert(nutricionista)
            return True
        except IntegrityError as e:
            raise EmailAlreadyRegistredError  
    


   


