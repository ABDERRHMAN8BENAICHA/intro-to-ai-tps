def sort_Length_of_the_Elements(list,length):
    index = length
    is_sorting = False
    while index > 0 and not is_sorting:
        is_sorting = True
        for i in range(index):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                is_sorting = False
    return list

# Test the function
list = [64, 34, 25, 12, 22, 11,30,99]
length = 5
print(sort_Length_of_the_Elements(list,length))