from funciones import calcular_iva, aplicar_descuento

def procesar_compra(precio_base, porcentaje_descuento=0, porcentaje_iva=16):
    """Proceso completo de integración para calcular el total final de una compra."""
    if precio_base <= 0:
        raise ValueError("El precio base debe ser mayor a cero")
    
    precio_con_descuento = aplicar_descuento(precio_base, porcentaje_descuento)
    monto_iva = calcular_iva(precio_con_descuento, porcentaje_iva)
    precio_total = precio_con_descuento + monto_iva
    
    return {
        "precio_base": precio_base,
        "descuento_aplicado": precio_base - precio_con_descuento,
        "iva": monto_iva,
        "total": precio_total
    }

if __name__ == "__main__":
    resultado = procesar_compra(100, 10, 16)
    print("Resultado de compra exitosa:", resultado)