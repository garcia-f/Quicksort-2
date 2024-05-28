def quick_sort(array):
    """
    Ordena un arreglo utilizando el algoritmo Quicksort.

    Parameters:
        array (list): El arreglo a ser ordenado.

    Returns:
        None: El arreglo se ordena in-place, por lo que no se devuelve nada.

    Example:
        >>> arr = [4, 6, 2, 5, 8, 1, 4, 12, 9, 5, 10]
        >>> quick_sort(arr)
        >>> print(arr)
        [1, 2, 4, 4, 5, 5, 6, 8, 9, 10, 12]
    """
    def _quick_sort(array, low, high):
        """
        Función auxiliar que realiza la ordenación recursiva del arreglo.

        Parameters:
            array (list): El arreglo a ser ordenado.
            low (int): Índice bajo del arreglo.
            high (int): Índice alto del arreglo.

        Returns:
            None: El arreglo se ordena in-place, por lo que no se devuelve nada.
        """
        if low < high:
            pi = partition(array, low, high)
            _quick_sort(array, low, pi - 1)
            _quick_sort(array, pi + 1, high)

    def partition(array, low, high):
        """
        Función que particiona el arreglo en base a un pivote.

        Parameters:
            array (list): El arreglo a ser particionado.
            low (int): Índice bajo del arreglo.
            high (int): Índice alto del arreglo.

        Returns:
            int: El índice del pivote después de la partición.
        """
        pivot = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[high] = array[high], array[i + 1]
        return i + 1

    _quick_sort(array, 0, len(array) - 1)

# Ejemplos de pruebas
if __name__ == "__main__":
    # Prueba 1
    arr1 = [4, 6, 2, 5, 8, 1, 4, 12, 9, 5, 10]
    print("Array original:", arr1)
    quick_sort(arr1)
    print("Array ordenado:", arr1)

    # Prueba 2
    arr2 = [10, 8, 3, 5, 2, 7, 6, 1, 4, 9]
    print("\nArray original:", arr2)
    quick_sort(arr2)
    print("Array ordenado:", arr2)

    # Prueba 3
    arr3 = [1, 2, 3, 4, 5]
    print("\nArray original:", arr3)
    quick_sort(arr3)
    print("Array ordenado:", arr3)
