def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1


def quickSort(array, low, high):
    if low < high:
        # pi is partitioning index
        pi = partition(array, low, high)

        # recursive call on the left of pivot
        quickSort(array, low, pi - 1)

        # recursive call on the right of pivot
        quickSort(array, pi + 1, high)


# main code

data = [1, 2, 5]

# data = input("Enter your element separated by , : ")

print("Unsorted Array:", data)

size = len(data)
quickSort(data, 0, size - 1)

print("Sorted Array in Ascending Order:", data)