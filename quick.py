def partition(list, low, high):
    i = low
    pivot = list[high]

    for j in range(low, high):
        if list[j] <= pivot:
            list[i], list[j] =  list[j], list[i]
            i += 1

    list[i], list[high] = list[high] ,list[i]

    return i

