import pytest

from unittest.mock import MagicMock

from app.models.cliente_model import Cliente
from app.services.auth.errors import EmailAlreadyRegistredError
from app.repository.cliente_repository import ClienteRepository

def test_insert(cliente_mocked):
    clienteRepository = ClienteRepository()
    clienteRepository.insert = MagicMock(return_value=True)

    result = clienteRepository.insert(cliente_mocked)

    clienteRepository.insert.assert_called_with(cliente_mocked)

    assert result == True
