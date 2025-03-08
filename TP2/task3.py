def class_odd_even(list):
    odd = []
    even = []
    for number in list:
        if number % 2 == 0:
            even.append(number)
        else:
            odd.append(number)
    return odd, even

# Test the function
numbers = [1, 2, 3, 4, 5]
odd, even = class_odd_even(numbers)
print("Odd numbers:", odd)
print("Even numbers:", even)