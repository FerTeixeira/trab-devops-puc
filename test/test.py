
from src.main import *
from unittest.mock import patch

import pytest
import pytest_asyncio

@pytest.mark.asyncio
async def test_root():
    result = await root()
    assert result == {"message": "Hello World"}

@pytest.mark.asyncio
async def test_funcaoteste():
    with patch('random.randint', return_value=12345):
        result = await funcaoteste()
    assert result == {"teste": True, "num_aleatorio": 12345}

@pytest.mark.asyncio
async def test_create_estudante():
    estudante_teste = Estudante(name="Fulano", curso="Curso 1", ativo=False)
    result = await create_estudante(estudante_teste)
    assert estudante_teste == result

@pytest.mark.asyncio
async def test_update_estudante_negativo():
    result = await update_estudante(-5)
    assert not result

@pytest.mark.asyncio
async def test_update_estudante_positivo():
    result = await update_estudante(10)
    assert result

@pytest.mark.asyncio
async def test_delete_estudante_negativo():
    result = await delete_estudante(-5)
    assert not result

@pytest.mark.asyncio
async def test_delete_estudante_positivo():
    result = await delete_estudante(5)
    assert result

@pytest.mark.asyncio
async def test_somar():
    result = await somar(2, 3)
    assert result == {"resultado": 5}

@pytest.mark.asyncio
async def test_subtrair():
    result = await subtrair(10, 4)
    assert result == {"resultado": 6}

@pytest.mark.asyncio
async def test_multiplicar():
    result = await multiplicar(3, 5)
    assert result == {"resultado": 15}

@pytest.mark.asyncio
async def test_dividir_normal():
    result = await dividir(8, 2)
    assert result == {"resultado": 4.0}

@pytest.mark.asyncio
async def test_dividir_por_zero():
    result = await dividir(5, 0)
    assert result == {"erro": "Divisão por zero não é permitida"}

@pytest.mark.asyncio
async def test_dobro():
    result = await dobro(7)
    assert result == {"resultado": 14}
