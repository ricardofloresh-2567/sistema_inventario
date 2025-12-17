"""
Sistema de Gestión de Inventario - Interfaz Principal
Aplicación interactiva para gestionar productos
"""

from mi_proyecto.models.producto import Libreria, Producto
from mi_proyecto.repositories.inventario import RepositorioMemoria, Inventario
from mi_proyecto.services.reportes import GeneradorReportes
from mi_proyecto.utils.validadores import Validadores
from mi_proyecto.utils.formatters import Formateadores

class AplicacionInventario:
    """Aplicación principal con interfaz de usuario."""
    
    def __init__(self):
        """Inicializa la aplicación."""
        self.repositorio = RepositorioMemoria()
        self.inventario = Inventario(self.repositorio)
        self.reportes = GeneradorReportes(self.inventario)
    
    def mostrar_menu_principal(self) -> str:
        """Muestra el menú principal."""
        print("\n" + "=" * 50)
        print("     SISTEMA DE GESTION DE INVENTARIO")
        print("=" * 50)
        print("1. Agregar producto")
        print("2. Ver todos los productos")
        print("3. Aumentar stock")
        print("4. Disminuir stock (Venta)")
        print("5. Productos con bajo stock")
        print("6. Ver reporte completo")
        print("7. Salir")
        print("=" * 50)
        
        return input("Seleccione una opción: ")
    
    def agregar_producto_interactivo(self):
        """Permite agregar un producto de forma interactiva."""
        try:
            print("\n--- AGREGAR NUEVO PRODUCTO ---")
            nombre = input("Nombre del producto: ")
            Validadores.validar_nombre_no_vacio(nombre)
            
            descripcion = input("Descripcion: ")
            
            precio = float(input("Precio: $"))
            Validadores.validar_precio_positivo(precio)
            
            cantidad = int(input("Cantidad inicial: "))
            Validadores.validar_cantidad_no_negativa(cantidad)
            
            print("\nCategorías disponibles:")
            categorias_lista = list(Libreria)
            for i, cat in enumerate(categorias_lista, 1):
                print(f"  {i}. {cat.value}")
            
            seleccion = input("\nSeleccione la categoría (número o nombre): ").strip()
            
            libreria = None
            try:

                num_seleccion = int(seleccion)
                if num_seleccion < 1 or num_seleccion > len(categorias_lista):
                    raise ValueError(f"Por favor seleccione un número entre 1 y {len(categorias_lista)}")
                libreria = categorias_lista[num_seleccion - 1]
            except ValueError:
                
                try:
                    cat_str = seleccion.upper().replace(" ", "_")
                    libreria = Libreria[cat_str]
                except KeyError:
                    raise ValueError(f"Categoría '{seleccion}' no encontrada. Use un número (1-{len(categorias_lista)}) o el nombre de la categoría.")
            
            producto = self.inventario.agregar_producto(nombre, descripcion, precio, cantidad, libreria)
            print(f"\nOK -  Producto agregado: {producto}")
            
        except (ValueError, KeyError, IndexError) as e:
            print(f"ERROR: {e}")
    
    def ver_todos_productos(self):
        """Muestra todos los productos."""
        productos = self.repositorio.obtener_todos()
        if productos:
            print(Formateadores.formatear_lista_productos(productos))
        else:
            print("\n" + "=" * 60)
            print(" " * 15 + "No hay productos en el inventario")
            print("=" * 60)
    
    def aumentar_stock_interactivo(self):
        """Aumenta el stock de un producto."""
        try:
            id_prod = int(input("ID del producto: "))
            cantidad = int(input("Cantidad a aumentar: "))
            
            self.inventario.aumentar_stock(id_prod, cantidad)
            print("OK - Stock aumentado exitosamente")
            
        except (ValueError, KeyError) as e:
            print(f"ERROR: {e}")
    
    def disminuir_stock_interactivo(self):
        """Disminuye el stock de un producto (simula venta)."""
        try:
            id_prod = int(input("ID del producto: "))
            cantidad = int(input("Cantidad vendida: "))
            
            self.inventario.disminuir_stock(id_prod, cantidad)
            print("OK  Venta registrada exitosamente")
            
        except (ValueError, KeyError) as e:
            print(f"ERROR: {e}")
    
    def ver_bajo_stock(self):
        """Muestra productos con bajo stock."""
        limite = int(input("Límite de stock bajo (default 10): ") or "10")
        productos = self.inventario.obtener_productos_bajo_stock(limite)
        print(Formateadores.formatear_lista_productos(productos))
        
    def ver_reporte(self):
        """Muestra el reporte completo."""
        reporte = self.reportes.reporte_completo()
        print(Formateadores.formatear_reporte(reporte))
    
    def ejecutar(self):
        """Ejecuta la aplicación principal."""
        self._cargar_datos_prueba()
        
        while True:
            opcion = self.mostrar_menu_principal()
            
            if opcion == "1":
                self.agregar_producto_interactivo()
            elif opcion == "2":
                self.ver_todos_productos()
            elif opcion == "3":
                self.aumentar_stock_interactivo()
            elif opcion == "4":
                self.disminuir_stock_interactivo()
            elif opcion == "5":
                self.ver_bajo_stock()
            elif opcion == "6":
                self.ver_reporte()
            elif opcion == "7":
                print("\n¡Hasta luego!")
                break
            else:
                print("\n¡ERROR - Opción inválida!")
    
    def _cargar_datos_prueba(self):
        """Carga datos de prueba en el inventario."""
        productos_prueba = [
            ("Lapiz", "Lapiz Artesco", 1.99, 50, Libreria.ESCRITURA),
            ("Mouse", "Mouse inalámbrico", 25.50, 50, Libreria.TECNOLOGIA),
            ("Sonaja", "Sonaja Agu", 20.00, 15, Libreria.JUGUETES),
            ("Tajador", "Tajador Binifan", 2.50, 100, Libreria.ESCRITURA),
            ("Muñeca", "Muñeca Alicia", 60.00, 30, Libreria.JUGUETES),
            ("Radio", "Radio Sony", 35.00, 25, Libreria.TECNOLOGIA),
            ("biblia", "Biblia Sagrado Testamento", 89.99, 18, Libreria.LIBROS),
        ]
        
        for nombre, desc, precio, cantidad, libreria in productos_prueba:
            self.inventario.agregar_producto(nombre, desc, precio, cantidad, libreria)
        
        print("\nOK - Datos de prueba cargados")

if __name__ == "__main__":
    app = AplicacionInventario()
    app.ejecutar()