"""Modulo de Modelos - Productos
    Define las entidades principales del sistema """
    

from datetime import datetime
from enum import Enum

class Libreria(Enum):
    """Enumeracion de categorias de utiles."""
    ESCRITURA = "Escritura"
    TECNOLOGIA = "Tecnologia"
    JUGUETES = "Juguetes"
    LIBROS = "Libros"
    MANUALIDADES = "Manualidades"
    ORGANIZADORES = "Organizadores"
    ACCESORIOS = "Accesorios"

class Producto:
    """
    Clase que representa un producto en el inventario
    """
    
    """
        Representa un producto en el inventario
        
        Atributos:
            codigo (str): Código único del producto
            nombre (str): Nombre del producto
            descripcion (str): Descripción del producto
            precio (float): Precio del producto
            cantidad (int): Cantidad disponible en inventario
        """
        
    _contador = 1000
    
    def __init__(self, nombre:str, descripcion:str, precio:float, cantidad: int, libreria:Libreria):
        
        """Inicializa un producto
        
        
        
        
        
        """
        if not nombre or not nombre.strip():
            raise ValueError("El nombre no puede estar vacio")
        if precio < 0:
            raise ValueError("El precio no puede ser negativo")
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")
        
        Producto._contador +=1
        
        self.id_producto = Producto._contador
        self.nombre = nombre.strip()
        self.descripcion = descripcion.strip()
        self.precio = precio
        self.cantidad = cantidad
        self.libreria = libreria
        self.fecha_creacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def actualizar_cantidad(self, cantidad: int) -> bool:
        """Actualiza la cantidad de producto."""
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")
        self.cantidad = cantidad
        return True
    
    def actualizar_precio(self, precio: float) -> bool:
        """Actualiza el precio del producto."""
        if precio < 0:
            raise ValueError("El precio no puede ser negativo")
        self.precio = precio
        return True
    
    def calcular_valor_total(self) -> float:
        """Calcula el valor total del producto en stock."""
        return self.precio * self.cantidad
    
    def __str__(self) -> str:
        """
        Representación en string del producto
        """
        return f"[{self.id_producto}] {self.nombre} - ${self.precio:.2f} (Stock: {self.cantidad})"
    
    
    def __repr__(self) ->str:
        """
        Representación técnica del producto
        
        Returns:
            str: Representación del objeto
        """
        return f"Producto(id='{self.id_producto}', nombre ='{self.nombre}', precio ={self.precio}, cantidad ='{self.cantidad}')"