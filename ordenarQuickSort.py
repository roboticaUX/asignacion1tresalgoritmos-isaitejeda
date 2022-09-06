#posición de partida
def partition(array, low, high):

  # elige el elemento más a la derecha como pivote
  pivot = array[high]

  # indicador del número más grande
  i = low - 1

  # recorrer todos los elementos 
  # para comparar cada elemento con el pivote
  for j in range(low, high):
    if array[j] <= pivot:
      # si se encuentra un elemento más pequeño que el pivote, 
      # cambia por el elemento mayor señalado por i
      i = i + 1

      # intercambio de elemento en i con elemento en j
      (array[i], array[j]) = (array[j], array[i])

  # intercambiar el elemento pivote con el elemento mayor especificado por i
  (array[i + 1], array[high]) = (array[high], array[i + 1])

  # devuelve la posición desde donde se realiza el punto de partida
  return i + 1

# ordenar
def quickSort(array, low, high):
  if low < high:

    #encuentra el número pivote tal que el número más pequeño 
    # que el pivote esté a la izquierda y el número mayor 
    # que el pivote esté a la derecha
    pi = partition(array, low, high)

    # llamada recursiva a la izquierda del pivote
    quickSort(array, low, pi - 1)

    # llamada recursiva a la izquierda del pivote
    quickSort(array, pi + 1, high)


data = [8, 3, 12, 4, 2, 9, 7, 1]
print("Unsorted Array")
print(data)

size = len(data)

quickSort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data)