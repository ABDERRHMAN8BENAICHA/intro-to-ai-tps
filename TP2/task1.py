def largest(list):
    if len(list) < 2:
        return None
    max = list[0]
    for number in list:
        if number >= max:
            max = number
    return max

# Test the function
numbers = [1, 2, 3, 4, 5]
print(largest(numbers))