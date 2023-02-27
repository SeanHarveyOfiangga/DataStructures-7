def insertion_sort(list):  
    for i in range(1, len(list)):  
        current = list[i]  

        j = i - 1  
        while j >= 0 and current < list[j]:  
            list[j+1] = list[j]  
            j -= 1  
        list[j+1] = current  

    return list

def main():
    list = [95, 7, 3, 18, 130, 9, -5, 75, 27, 25, 15, 5, 11, 69, 39, 4, 8, 14]
    insertion_sort(list)
    print(list)

    list = [7, 5, 8, 2]
    insertion_sort(list)
    print(list)

main()