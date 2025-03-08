def bubble_sort(list):
    index = len(list)-1
    is_sorting = False
    while index > 0 and not is_sorting:
        is_sorting = True
        for i in range(index):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                is_sorting = False
    return list

def find_second_largest(list):
    if len(list) < 2:
        return None
    list = bubble_sort(list)
    return list[-2]

# Test the function
print(find_second_largest([5, 2, 8, 1, 9]))