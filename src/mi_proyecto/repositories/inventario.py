from abc import ABC, abstractmethod
from typing import List, Optional, Dict
from ..models.producto import Producto, Libreria


class IRepositorio(ABC):
    """
    Interfaz que define las operaciones básicas de un repositorio
    """
    
    @abstractmethod
    def agregar(self, producto: Producto) -> bool:
        """Agrega un producto al repositorio"""
        pass
    
    @abstractmethod
    def obtener(self, id_producto: int) -> Optional[Producto]:
        """Obtiene un producto por su ID"""
        pass
    
    @abstractmethod
    def obtener_todos(self) -> List[Producto]:
        """Obtiene todos los productos"""
        pass
    
    @abstractmethod
    def eliminar(self, id_producto: int) -> bool:
        """Elimina un producto por su ID"""
        pass

class RepositorioMemoria(IRepositorio):
    """
    Implementación del repositorio que almacena productos en memoria 
    """
    
    def __init__(self):
        """inicializa el diccionario de productos"""
        self._productos: Dict[int, Producto] = {}
    
    def agregar(self, producto: Producto) -> bool:
        """
        Agrega un producto al repositorio
        """
        if producto.id_producto in self._productos:
            raise ValueError(f"El producto con ID {producto.id_producto} ya existe")
        self._productos[producto.id_producto] = producto
        return True
    
    def obtener(self, id_producto: int) -> Optional[Producto]:
        """
        Obtiene un producto por su ID.
        """
        return self._productos.get(id_producto)
    
    def obtener_todos(self) -> List[Producto]:
        """
        Obtiene todos los productos.
        """
        return list(self._productos.values())
    
    def eliminar(self, id_producto: int) -> bool:
        """
        Elimina un producto del repositorio
        """
        if id_producto in self._productos:
            del self._productos[id_producto]
            return True
        return False
    
    def obtener_por_libreria(self, libreria: Libreria) -> List[Producto]:
        """Obtiene productos por categoría."""
        return [p for p in self._productos.values() if p.libreria == libreria]


class Inventario:
    """
    Clase que gestiona el inventario de productos utilizando un repositorio
    """
    
    def __init__(self, repositorio: IRepositorio):
        """
        Constructor del inventario
        """
        self.repositorio = repositorio
    
    def agregar_producto(self, nombre: str, descripcion: str, precio: float, cantidad: int, libreria: Libreria) -> Producto:
        """
        Agrega un nuevo producto al inventario
        """
        producto = Producto(nombre, descripcion, precio, cantidad, libreria)
        self.repositorio.agregar(producto)
        return producto

    def aumentar_stock(self, id_producto: int, cantidad: int) -> bool:
        """Aumenta el stock de un producto."""
        producto = self.repositorio.obtener(id_producto)
        if not producto:
            raise ValueError(f"Producto con ID {id_producto} no existe")
        
        producto.actualizar_cantidad(producto.cantidad + cantidad)
        return True
    
    def disminuir_stock(self, id_producto: int, cantidad: int) -> bool:
        """Disminuye el stock de un producto (venta)."""
        producto = self.repositorio.obtener(id_producto)
        if not producto:
            raise ValueError(f"Producto con ID {id_producto} no existe")
        
        if producto.cantidad < cantidad:
            raise ValueError(f"Stock insuficiente. Disponible: {producto.cantidad}")
        
        producto.actualizar_cantidad(producto.cantidad - cantidad)
        return True
    
    def obtener_productos_bajo_stock(self, limite: int = 10) -> List[Producto]:
        """Obtiene productos con stock bajo."""
        return [p for p in self.repositorio.obtener_todos() if p.cantidad <= limite]