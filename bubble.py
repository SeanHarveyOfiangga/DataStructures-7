def bubble_sort(list):
    n = len(list)

    for i in range(n-1):
        for j in range(n-1):
            if list[j] > list[j+1]: 
                tmp = list[j]
                list[j] = list[j+1]
                list[j+1] = tmp

    return list

def main():
    list = [95, 7, 3, 18, 130, 9, -5, 75, 27, 25, 15, 5, 11, 69, 39, 4, 8, 14]
    bubble_sort(list)
    print(list)

    list = [7, 5, 8, 2]
    bubble_sort(list)
    print(list)

main()