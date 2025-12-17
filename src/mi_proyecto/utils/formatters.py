"""
    Módulo de Utilidades - Formateadores
    Define funciones para formatear y presentar datos
"""

from typing import List, Dict, Any
from ..models.producto import Producto

class Formateadores:
    """Clase con métodos estáticos para formatear datos."""
    
    @staticmethod
    def formatear_precio(precio: float) -> str:
        """Formatea precio con símbolo de moneda."""
        return f"${precio:.2f}"
    
    @staticmethod
    def formatear_producto_tabla(producto: Producto) -> str:
        """Formatea producto para visualización en tabla."""
        
        nombre = producto.nombre[:25] if len(producto.nombre) > 25 else producto.nombre
        descripcion = producto.descripcion[:35] if len(producto.descripcion) > 35 else producto.descripcion
        categoria = producto.libreria.value[:15] if len(producto.libreria.value) > 15 else producto.libreria.value
        
        if len(producto.nombre) > 25:
            nombre = nombre[:22] + "..."
        if len(producto.descripcion) > 35:
            descripcion = descripcion[:32] + "..."
        if len(producto.libreria.value) > 15:
            categoria = categoria[:12] + "..."
        
        return (f"| {producto.id_producto:>4} | {nombre:<25} | {descripcion:<35} | "
                f"{categoria:<15} | ${producto.precio:>9.2f} | {producto.cantidad:>5} | "
                f"${producto.calcular_valor_total():>12.2f} |")
    
    @staticmethod
    def formatear_lista_productos(productos: List[Producto]) -> str:
        """Formatea lista de productos para mostrar"""
        if not productos:
            return "\n" + "=" * 100 + "\n" + " " * 40 + "No hay productos para mostrar\n" + "=" * 100
        
        ancho_tabla = 130
        separador = "=" * ancho_tabla
        separador_linea = "-" * ancho_tabla
        

        output = "\n" + separador + "\n"
        output += " " * 45 + "LISTA DE PRODUCTOS\n"
        output += separador + "\n"
        
        encabezado = (f"| {'ID':>4} | {'Nombre':<25} | {'Descripción':<35} | "
                     f"{'Categoría':<15} | {'Precio':>11} | {'Stock':>4} | "
                     f"{'Valor Total':>12} |")
        
        output += encabezado + "\n"
        output += separador_linea + "\n"
        
        filas = [Formateadores.formatear_producto_tabla(p) for p in productos]
        output += "\n".join(filas)
        
        output += "\n" + separador_linea + "\n"
        
        total_productos = len(productos)
        total_stock = sum(p.cantidad for p in productos)
        valor_total = sum(p.calcular_valor_total() for p in productos)
        
        output += f"\n{'RESUMEN:':<20} {total_productos} producto(s) | "
        output += f"Stock total: {total_stock} unidades | "
        output += f"Valor total: ${valor_total:,.2f}\n"
        output += separador + "\n"
        
        return output
    
    @staticmethod
    def formatear_reporte(reporte: Dict[str, Any]) -> str:
        """Formatea reporte para visualización"""
        output = "\n" + "=" * 60 + "\n"
        output += "           REPORTE DE INVENTARIO\n"
        output += "=" * 60 + "\n"
        output += f"Fecha: {reporte['fecha_generacion']}\n\n"
        output += f"Total de Productos: {reporte['total_productos']}\n"
        output += f"Total de Ítems en Stock: {reporte['total_items']}\n"
        output += f"Valor Total del Inventario: {reporte['valor_total']:.2f}\n\n"
        
        if reporte['producto_mas_caro']:
            output += f"Producto Más Caro: {reporte['producto_mas_caro'].nombre} "
            output += f"(${reporte['producto_mas_caro'].precio:.2f})\n"
        
        if reporte['producto_mas_barato']:
            output += f"Producto Más Barato: {reporte['producto_mas_barato'].nombre}"
            output += f" (${reporte['producto_mas_barato'].precio:.2f})\n"
        
        output += f"\nProductos Bajo Stock: ({len(reporte['productos_bajo_stock'])})\n"
        output += "=" * 60 + "\n"
        
        return output