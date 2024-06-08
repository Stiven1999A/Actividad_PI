"""Construcción Clase Vehículo."""

class Vehiculo:
    """Esta es una clase llamada vehículo que
      recibe atributos: marca, modelo y año de 
      lanzamiento de un vehículo.
    """
    def __init__(self, marca, modelo, year):
        self.__marca = marca
        self.__modelo = modelo
        self.__year = year

    # Métodos para acceder a los atributos privados
    def get_marca(self):
        """
        Obtiene la marca del vehículo.

        Returns:
            str: La marca del vehículo.
        """
        return self.__marca

    def get_modelo(self):
        """
        Obtiene el modelo del vehículo.

        Returns:
            str: El modelo del vehículo.
        """
        return self.__modelo

    def get_year(self):
        """Obtiene el año del vehículo.
         
         Returns:
            int: El año del vehículo.
         """
        return self.__year

    def set_marca(self, nueva_marca):
        """Establece la marca del vehículo con el valor proporcionado.

        Args:
        nueva_marca (str): La nueva marca que se asignará al vehículo.
        
        Returns:
            None
        """
        self.__marca = nueva_marca

    def set_modelo(self, nuevo_modelo):
        """ 
        Establece el nuevo modelo del vehículo.
        
        Args:
            nuevo_modelo (str): El nuevo modelo que se asignará al vehículo.
            
            Returns:
                None
        """
        self.__modelo = nuevo_modelo

    def set_year(self, nuevo_year):
        """
        Establece el nuevo año del vehículo.
        
        Args:
            nuevo_year (int): El nuevo año que se asignará al vehículo.
        
        Returns:
            None
        """
        self.__year = nuevo_year

    def detalles(self):
        """
        Devuelve una cadena con los detalles del vehículo.
        
        Returns:
            str: Una cadena que contiene la marca, modelo y año del vehículo.
        """

        return f"Marca: {self.get_marca()}, Modelo: {self.get_modelo()}, Año: {self.get_year()}"
    