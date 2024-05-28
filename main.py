# función principal que se llama para ordenar el arreglo
def quick_sort(array):
    # función auxiliar que realiza la ordenación recursiva del arreglo
    def _quick_sort(array, low, high):
        if low < high:
            pi = partition(array, low, high)
            _quick_sort(array, low, pi - 1)
            _quick_sort(array, pi + 1, high)

    # esta función realiza la partición del arreglo en base a un pivote
    def partition(array, low, high):
        pivot = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] <= pivot:
                i = i + 1
                (array[i], array[j]) = (array[j], array[i])
        (array[i + 1], array[high]) = (array[high], array[i + 1])
        return i + 1

    _quick_sort(array, 0, len(array) - 1)

# arreglo inicial
arr = [4, 6, 2, 5, 8, 1, 4, 12, 9, 5, 10]
print("Array original:", arr)

quick_sort(arr)
print("Array ordenado:", arr)