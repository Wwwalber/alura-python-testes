import pytest
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# para garantir que o python encontre o módulo user_model

from models.user_model import serialize_user # para 

def test_serialize_user_completo():
    user = {
        "email": "teste@exemplo.com",
        "name": "Usuário de Teste",
        "address": "Rua dos Testes, 123",
        "role": "admin"
    }
    resultado = serialize_user(user)
    esperado = {
        "email": "teste@exemplo.com",
        "name": "Usuário de Teste",
        "address": "Rua dos Testes, 123",
        "role": "admin"
    }
    assert resultado == esperado

