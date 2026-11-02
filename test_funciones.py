import pytest
from funciones import calcular_iva, aplicar_descuento

def test_calcular_iva():
    assert calcular_iva(100) == 16.0
    assert calcular_iva(200, 8) == 16.0

def test_aplicar_descuento():
    assert aplicar_descuento(100, 10) == 90.0
    assert aplicar_descuento(50, 50) == 25.0

def test_valores_negativos():
    with pytest.raises(ValueError):
        calcular_iva(-100)