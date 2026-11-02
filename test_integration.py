import pytest
from main import procesar_compra

def test_procesar_compra_exito_try():
    """Prueba de integración exitosa (Bloque Try/Exitoso)."""
    try:
        resultado = procesar_compra(100, 10, 16)
        assert resultado["precio_base"] == 100
        assert resultado["descuento_aplicado"] == 10.0
        assert resultado["iva"] == 14.4
        assert resultado["total"] == 104.4
    except Exception as e:
        pytest.fail(f"La integración falló inesperadamente: {e}")

def test_procesar_compra_error_exception():
    """Prueba de integración con manejo de excepción (Bloque Exception)."""
    with pytest.raises(ValueError) as exc_info:
        procesar_compra(-50, 10, 16)
    assert "El precio base debe ser mayor a cero" in str(exc_info.value)