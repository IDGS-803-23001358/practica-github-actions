def calcular_iva(precio, porcentaje_iva=16):
    """Calcula el IVA de un precio dado."""
    if precio < 0:
        raise ValueError("El precio no puede ser negativo")
    return precio * (porcentaje_iva / 100)

def aplicar_descuento(precio, porcentaje_descuento):
    """Calcula el precio final aplicando un descuento."""
    if precio < 0 or porcentaje_descuento < 0 or porcentaje_descuento > 100:
        raise ValueError("Valores fuera de rango")
    descuento = precio * (porcentaje_descuento / 100)
    return precio - descuento