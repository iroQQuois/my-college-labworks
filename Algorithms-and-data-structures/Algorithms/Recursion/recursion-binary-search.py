def recursion_binary_search(array=[1, 3, 4, 5, 6, 7, 8], key=7):
    left = 0
    right = array.index(array[-1])
    if right < left:
        return None

    mid = (left + right) // 2
    if (left + right) % 2 == 1:
        mid += 1
    if array[mid] > key:
        return recursion_binary_search(array[:mid], key)
    elif array[mid] < key:
        return mid + recursion_binary_search(array[mid:], key)
    else:
        return mid
