#implementar casos de teste para a função serialize_product
import pytest
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) # isso possibilita o import do arquivo models.user_model

from models.product_model import serialize_product

# Serialização para retorno de produtos #Arrange
def test_serialize_product_valido():
    product = {
        "_id": "507f1f77bcf86cd799439011",
        "name": "Produto de Teste",
        "description": "Descrição do produto de teste",
        "category": "Categoria de teste",
        "price": 100.0,
        "available": True,
        "ingredients": ["pão","carne","queijo"]
    }
    resultado = serialize_product(product) #Act
    esperado = {
        "id": "507f1f77bcf86cd799439011",
        "name": "Produto de Teste",
        "description": "Descrição do produto de teste",
        "category": "Categoria de teste",
        "price": 100.0,
        "available": True,
        "ingredients": ["pão","carne","queijo"]
    }
    # Assert
    assert resultado == esperado

def test_serialize_product_sem_ingredientes():
    product = {
        "_id": "507f1f77bcf86cd799439011",
        "name": "Produto de Teste",
        "description": "Descrição do produto de teste",
        "category": "Categoria de teste",
        "price": 100.0,
        "available": True,
        "ingredients": []
    }
    resultado = serialize_product(product) #Act
    esperado = {
        "id": "507f1f77bcf86cd799439011",
        "name": "Produto de Teste",
        "description": "Descrição do produto de teste",
        "category": "Categoria de teste",
        "price": 100.0,
        "available": True,
        "ingredients": []
    }
    # Assert
    assert resultado == esperado

def test_serialize_product_incompleto():
    product = {
        "_id": "507f1f77bcf86cd799439011",
        "name": "Produto de Teste",
    }
    resultado = serialize_product(product) #Act
    esperado = {
        "id": "507f1f77bcf86cd799439011",
        "name": "Produto de Teste",
        "description": None,
        "category": None,
        "price": None,
        "available": True,
        "ingredients": []
    }
    # Assert
    assert resultado == esperado
    
def test_serialize_product_vazio():
    product = {}
    resultado = serialize_product(product) #Act
    esperado = {
        "id": "None",
        "name": None,
        "description": None,
        "category": None,
        "price": None,
        "available": True,
        "ingredients": []
    }
    # Assert
    assert resultado == esperado

# casos que geram exceções
def test_serialize_product_inteiro():
    with pytest.raises(AttributeError): #Arrange
        serialize_product(123456789) #Act

def test_serialize_product_string():
    with pytest.raises(AttributeError): #Arrange
        serialize_product("string de teste") #Act

def test_serialize_product_lista():
    with pytest.raises(AttributeError): #Arrange
        serialize_product(["item1", "item2", "item3"]) #Act

def test_serialize_product_booleano():
    with pytest.raises(AttributeError): #Arrange
        serialize_product(True) #Act

def test_serialize_product_None():
    with pytest.raises(AttributeError): #Arrange
        serialize_product(None) #Act
        
# casos dos tipos inesperados no input
def test_serialize_product_inesperado():
    product = {
        "_id": 123456789,
        "name": ["nome","do", "produto"],
        "description": {"detalhe":"objeto"},
        "category": 9999,
        "price": "cem reais",
        "available": "sim",
        "ingredients": "Não é lista"
    }
    resultado = serialize_product(product) #Act
    esperado = {
        "id": "123456789", # id vira string
        "name": ["nome", "do", "produto"],
        "description": {"detalhe":"objeto"},
        "category": 9999,
        "price": "cem reais",
        "available": "sim",
        "ingredients": "Não é lista"
    }
    assert resultado == esperado
    
def test_serialize_product_dict_none():
    product = {
        "_id": None,
        "name": None,
        "description": None,
        "category": None,
        "price": None,
        "available": None,
        "ingredients": None
    }   
    resultado = serialize_product(product) #Act
    esperado = {
        "id": "None",
        "name": None,
        "description": None,
        "category": None,
        "price": None,
        "available": None,
        "ingredients": None
    }   
    assert resultado == esperado
        
        