"""
Módulo de Utilidades - Validadores
Define funciones para validar entrada de datos
"""


from typing import List

class Validadores:
    """Clase con métodos estáticos para validaciones."""
    
    @staticmethod
    def validar_precio_positivo(precio: float) -> bool:
        """Valida que el precio sea positivo."""
        if not isinstance(precio, (int, float)):
            raise ValueError("El precio debe ser un número")
        if precio < 0:
            raise ValueError("El precio no puede ser negativo")
        return True
    
    @staticmethod
    def validar_cantidad_no_negativa(cantidad: int) -> bool:
        """Valida que la cantidad no sea negativa."""
        if not isinstance(cantidad, int):
            raise ValueError("La cantidad debe ser un número entero")
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")
        return True
    
    @staticmethod
    def validar_nombre_no_vacio(nombre: str) -> bool:
        """Valida que el nombre no esté vacío."""
        if not isinstance(nombre, str):
            raise ValueError("El nombre debe ser texto")
        if not nombre or not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")
        return True
    
    @staticmethod
    def validar_libreria_valida(libreria: str, librerias_validas: List[str]) -> bool:
        """Valida que la categoría esté en la lista de categorías válidas."""
        if libreria not in librerias_validas:
            raise ValueError(f"Categoría inválida. Válidas: {', '.join(librerias_validas)}")
        return True