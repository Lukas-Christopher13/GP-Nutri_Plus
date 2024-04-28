import pytest
from app.forms import ActivityForm

@pytest.fixture
def client():
    pass

def test_activity_form_fields():
    form = ActivityForm()
    assert hasattr(form, 'nome_atividade')
    assert hasattr(form, 'duracao')
    assert hasattr(form, 'intensidade')
    assert hasattr(form, 'data_atividade')

def test_activity_form_validations():
    form = ActivityForm()
    assert form.validate_on_submit() is False

    
    form.nome_atividade.data = 'Caminhada'
    form.duracao.data = 30
    form.intensidade.data = 'Moderada'
    form.data_atividade.data = '2024-04-11'
    assert form.validate_on_submit() is True

    form.nome_atividade.data = ''
    assert form.validate_on_submit() is False
