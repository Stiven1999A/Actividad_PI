""""Aqui desarrollamos la función para calcular la suma de los primos hasta un número entero n."""
def suma_primos(n):
    """
    Calcula la suma de todos los números primos menores o iguales a n.

    Args:
        n (int): El número límite.

    Returns:
        int: La suma de los números primos.
    """
    def es_primo(num):
        """
        Verifica si un número es primo.

        Args:
            num (int): El número a verificar.

        Returns:
            bool: True si es primo, False si no lo es.
        """
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    suma = 0
    for i in range(2, n + 1):
        if es_primo(i):
            suma += i
    return suma
