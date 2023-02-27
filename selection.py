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

def main():
    list = [95, 7, 3, 18, 130, 9, -5, 75, 27, 25, 15, 5, 11, 69, 39, 4, 8, 14]
    selection_sort(list)
    print(list)

    list = [7, 5, 8, 2]
    selection_sort(list)
    print(list)

main()