def merge_sort(list):
    length = len(list)

    if length == 1:
        return list

    mid = length // 2

    left = merge_sort(list[:mid])
    right = merge_sort(list[mid:])

    return merge(left, right)

def merge(left, right):
    output = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1

    output.extend(left[i:])
    output.extend(right[j:])

    return output

def main():
    unsorted = [95, 7, 3, 18, 130, 9, -5, 75, 27, 25, 15, 5, 11, 69, 39, 4, 8, 14]
    sorted = merge_sort(unsorted)
    print(sorted)

    unsorted = [7, 5, 8, 2]
    sorted = merge_sort(unsorted)
    print(sorted)

main()