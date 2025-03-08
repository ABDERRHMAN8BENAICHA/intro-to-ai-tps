def intersection_two_list(list1, list2):
    return list(set(list1) & set(list2))

# Test the function
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 2, 6, 7, 8]
print(intersection_two_list(list1, list2))  
