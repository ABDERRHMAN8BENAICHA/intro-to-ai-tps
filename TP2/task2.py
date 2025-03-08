def second_largest(list):
    if len(list) < 2:
        return None
    max = list[0]
    second_max = list[0]
    for number in list:
        if number >= max:
            second_max = max
            max = number
        elif number > second_max:
            second_max = number
    return second_max

# Test the function
numbers = [1, 2, 3, 4, 5]
print(second_largest(numbers))