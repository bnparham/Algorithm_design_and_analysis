def partition(array:list, start, end, pivot_number):
    if pivot_number not in array : raise ValueError('pivot number not exist in array !')
    pivot = array.index(pivot_number)

    pivot_number = array.pop(pivot)
    array.append(pivot_number)

    pivot = end
    
    i = start - 1
    for j in range(start, end):
        if array[j] <= array[pivot]:
            i += 1
            (array[j], array[i]) = (array[i], array[j])
    (array[i + 1], array[end]) = (array[end], array[i + 1])
    return i + 1


def quick_sort(array, start_i, end_i):
    if start_i < end_i :
        q = partition(array, start_i, end_i, array[-1])
        quick_sort(array, start_i, q - 1)
        quick_sort(array, q + 1, end_i)

data = [5, 22, 33, 13, 7, 19, 27, 14, 27]

print("Unsorted Array")
print(data)

quick_sort(data, 0, len(data) - 1)

print('Sorted Array in Ascending Order:')
print(data)