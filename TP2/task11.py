import math

def find_perfect_squares_with_digit_sum(num_list):
    perfect_squares = []
    
    for num in num_list:
        if math.isqrt(num) ** 2 == num:
            digit_sum = sum(int(digit) for digit in str(num))
            if digit_sum < 10:
                perfect_squares.append(num)
    
    return perfect_squares

# # Test the function

print(find_perfect_squares_with_digit_sum([1, 4, 9, 16, 25, 36, 49, 64, 81, 100]))