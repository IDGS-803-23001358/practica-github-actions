import pytest
from main import procesar_compra

def test_sistema_flujo_completo_try():
    """Prueba a nivel de sistema para un flujo de compra completo."""
    try:
        compra1 = procesar_compra(200, 20, 16)
        assert compra1["total"] == 185.6
        
        compra2 = procesar_compra(500, 0, 16)
        assert compra2["total"] == 580.0
    except Exception as e:
        pytest.fail(f"Fallo en el flujo del sistema: {e}")

def test_sistema_error_acumulado_exception():
    """Prueba del sistema ante un fallo de valor no válido."""
    with pytest.raises(ValueError):
        procesar_compra(100, 150, 16)  # Descuento inválido mayor a 100%