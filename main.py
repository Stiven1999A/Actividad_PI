""" 1) Ejemplo de uso de la clase vehículo.
    2) Ejemplo de uso de la función para sumar los primos hasta un número n.
    3)"""

from vehiculo import Vehiculo
from primos import suma_primos
from api import get_users
#1)
mi_auto = Vehiculo(marca="Toyota", modelo="Corolla", year=2022)
print(mi_auto.detalles())
mi_auto.set_marca("Honda")
mi_auto.set_modelo("Camry")
mi_auto.set_marca(2020)
print(mi_auto.detalles())
#2)
print(f"La suma de los números primos hasta 30 es: {suma_primos(30)}")
#3)
print(get_users())
