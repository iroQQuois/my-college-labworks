none_sorted_array = [42, 545, 123, 34, 45, 666] 
sorted_array = [1,5,15,16,56,76,787,89978]


def linear_search(array, key):
  """
  DONE
  """
  if key in array:
    return array.index(key)
  else:
    return -1


#print(linear_search(none_sorted_array, int(input('Введите число, которое ищем в массиве: '))))


def ordered_linear_search(array, key):
  """
  DONE
  """
  for i in array:
    if key in array:
      return array.index(key)
    elif i <= 2:
      return -1 

#print(ordered_linear_search(sorted_array, int(input('Введите число, которое ищем в массиве: '))))


def binary_search(array=[1,2,3,4,5,6,7,9], key=8): # array - массив, в котором ищем, key - искомое число 
  """
  DONE
  """
  left = 0 # левая граница
  right = array.index(array[-1]) # правая граница   
  mid = (left + right) // 2 # средний элемент
  while array[mid] != key and left <= right:
    if key > array[mid]:
      left = mid + 1 # если искомое больше среднего элемента, то сдвиг идёт в правую сторону
    else:
      right = mid - 1 # если искомое меньше среднего элемента, то сдвиг идёт в левую сторону
    mid = (left + right) // 2 
  
  if left > right:
    return -1
  else:
    return mid


#print(binary_search(sorted_array, int(input('Введите число, которое ищем в массиве: '))))
    


def recursion_binary_search(array: list, val: int):
    low = 0
    high = len(array) - 1
    if high < low:
        return None

    mid = (low + high) // 2
    if (low + high) % 2 == 1:
        mid += 1
    if array[mid] > val:
        return binary_search(array[:mid], val)
    elif array[mid] < val:
        return mid + binary_search(array[mid:], val)
    else:
        return mid