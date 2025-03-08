def cumulative_sum(num_list):
    sum_list = []
    current_sum = 0  

    for num in num_list:
        current_sum += num  
        sum_list.append(current_sum)  

    return sum_list 

# Test the function
numbers = [1, 2, 3, 4, 5]
print(cumulative_sum(numbers))  
