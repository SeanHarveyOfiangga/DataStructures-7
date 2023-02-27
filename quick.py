def partition(list, low, high):
    i = low
    pivot = list[high]

    for j in range(low, high):
        if list[j] <= pivot:
            list[i], list[j] =  list[j], list[i]
            i += 1

    list[i], list[high] = list[high] ,list[i]

    return i

def quick_sort(list, low, high):
    if low < high:
        partition_index = partition(list, low, high)
        quick_sort(list, low, partition_index - 1)
        quick_sort(list, partition_index + 1, high)

def main():
    list = [95, 7, 3, 18, 130, 9, -5, 75, 27, 25, 15, 5, 11, 69, 39, 4, 8, 14]
    quick_sort(list, 0, len(list) - 1)
    print(list)

    list = [7, 5, 8, 2]
    quick_sort(list, 0, len(list) - 1)
    print(list)

main()