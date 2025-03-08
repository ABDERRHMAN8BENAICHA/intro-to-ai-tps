def sort_list(list):
    if len(list) == 0:
        return []
    elif len(list[0]) == 1:
        if list[0] > list[1]:
            return [list[1], list[0]]
    for i in list :
        if i[0] > i[1]:
            i[0],i[1] = i[1],i[0]
    return list

#Test the function
list = [[9, 6], [9, 8], [2, 4],[8, 5], [3, 9], [9, 2]]
print(sort_list(list))