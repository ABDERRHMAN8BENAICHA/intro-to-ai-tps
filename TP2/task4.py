numbers2 = [1, 2, 3, 4, 5]
numbers1 = [6,7,8,9,10]

def merge(list1, list2):
    new_numbers = []
    for i in range(len(list1)):
        new_numbers.append(list1[i])
    for i in range(len(list2)):
        new_numbers.append(list2[i])
    return new_numbers

def sorting(list):
    if len(list) < 2:
        return None
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
    return list

# Test the function
new_list = merge(numbers1, numbers2)
sorting(new_list)
print(new_list)
