from unittest.mock import MagicMock

from app.repository.nutricionista_repository import NutricionistaRepository
from app.services.auth.register_service import NutricionistaRegisterService

def test_register_an_nutricionista(nutricionista_mocked):    
    nutricionista_repository_mock = NutricionistaRepository()
    nutricionista_repository_mock.insert = MagicMock(return_value=True)

    nutricionista_service = NutricionistaRegisterService(nutricionista_repository_mock)

    #metodo testado
    result = nutricionista_service.register(nutricionista_mocked)

    nutricionista_repository_mock.insert.assert_called_with(nutricionista_mocked)
    
    assert result == True