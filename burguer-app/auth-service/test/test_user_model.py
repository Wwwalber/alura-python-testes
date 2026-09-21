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

def test_serialize_user_incompleto():
    user = {
        "email": "teste@exemplo.com",
    }
    resultado = serialize_user(user)
    esperado = {
        "email": "teste@exemplo.com",
        "name": "",
        "address": "",
        "role": "cliente"
    }
    assert resultado == esperado

def test_serialize_user_vazio():
    user = {}
    resultado = serialize_user(user)
    esperado = {
        "email": None,
        "name": "",
        "address": "",
        "role": "cliente"
    }
    assert resultado == esperado

def test_serialize_user_inteiro():
    with pytest.raises(AttributeError):
        serialize_user(12345)

def test_serialize_user_lista():
    with pytest.raises(AttributeError):
        serialize_user("String de teste")        

def test_serialize_user_none():
    with pytest.raises(AttributeError):
        serialize_user(None)

def test_serialize_user_inesperado():
    user = {
        "email": "123456",
        "name": ["nome","sobrenome"],
        "address":{"rua": "Rua de exemplo"},
        "role": True
    } 
    resultado = serialize_user(user) 
    esperado = {  
        "email": "123456",
        "name": ["nome","sobrenome"], 
        "address":{"rua": "Rua de exemplo"},
        "role": True
    }
    assert resultado == esperado

def test_serialize_user_dict_none():
    user = {
        "email": None,
        "name": None,
        "address": None,
        "role": None
    }
    resultado = serialize_user(user)
    esperado = {
        "email": None,
        "name": None,
        "address": None,
        "role": None
    }
    assert resultado == esperado

