def bubble_sort(list):
    n = len(list)

    for i in range(n-1):
        for j in range(n-1):
            if list[j] > list[j+1]: 
                tmp = list[j]
                list[j] = list[j+1]
                list[j+1] = tmp

    return list