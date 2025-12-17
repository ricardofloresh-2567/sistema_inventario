"""
Módulo de Servicios - Reportes
Define la lógica de generación de reportes y análisis
"""

from typing import List, Dict, Any, Optional
from datetime import datetime
from ..models.producto import Producto
from ..repositories.inventario import Inventario

class GeneradorReportes:
    """
    Genera reportes del inventario.
    Responsable de análisis y estadísticas.
    """
    
    def __init__(self, inventario: Inventario):
        """Inicializa el generador de reportes."""
        self.inventario = inventario
    
    def valor_total_inventario(self) -> float:
        """Calcula el valor total del inventario."""
        productos = self.inventario.repositorio.obtener_todos()
        return sum(p.calcular_valor_total() for p in productos)
    
    def cantidad_total_productos(self) -> int:
        """Retorna la cantidad total de productos."""
        return len(self.inventario.repositorio.obtener_todos())
    
    def total_items_stock(self) -> int:
        """Calcula el total de ítems en stock."""
        productos = self.inventario.repositorio.obtener_todos()
        return sum(p.cantidad for p in productos)
    
    def producto_mas_caro(self) -> Optional[Producto]:
        """Obtiene el producto más caro."""
        productos = self.inventario.repositorio.obtener_todos()
        return max(productos, key=lambda p: p.precio) if productos else None
    
    def producto_mas_barato(self) -> Optional[Producto]:
        """Obtiene el producto más barato."""
        productos = self.inventario.repositorio.obtener_todos()
        return min(productos, key=lambda p: p.precio) if productos else None
    
    def reporte_completo(self) -> Dict[str, Any]:
        """Genera reporte completo del inventario."""
        return {
            "fecha_generacion": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "total_productos": self.cantidad_total_productos(),
            "total_items": self.total_items_stock(),
            "valor_total": self.valor_total_inventario(),
            "producto_mas_caro": self.producto_mas_caro(),
            "producto_mas_barato": self.producto_mas_barato(),
            "productos_bajo_stock": self.inventario.obtener_productos_bajo_stock()
        }