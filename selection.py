def selection_sort(list):
    n = len(list)

    for i in range(n-1): 
        min = i

        for j in range(i+1, n):
            if list[j] < list[min]:
                min = j

        if min != i:
            temp = list[i]
            list[i] = list[min]
            list[min] = temp

    return list