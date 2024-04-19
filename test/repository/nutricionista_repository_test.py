from unittest.mock import MagicMock
from app.repository.nutricionista_repository import NutricionistaRepository


def test_insert(nutricionista_mocked):
    nutricionistaRepository = NutricionistaRepository()
    nutricionistaRepository.insert = MagicMock(return_value=True)

    result = nutricionistaRepository.insert(nutricionista_mocked)

    nutricionistaRepository.insert.assert_called_with(nutricionista_mocked)

    assert result

def test_insert_fail(nutricionista_mocked):
    nutricionistaRepository = NutricionistaRepository()
    nutricionistaRepository.insert = MagicMock(return_value=False)

    result = nutricionistaRepository.insert(nutricionista_mocked)

    nutricionistaRepository.insert.assert_called_with(nutricionista_mocked)

    assert result == False