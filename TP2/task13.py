import random  

def generate_random_numbers(n):
    random_list = []  
    for _ in range(n):
        random_number = random.randint(1, 20)  
        random_list.append(random_number) 
    return random_list  

# Test the function
numbers = generate_random_numbers(10)  
print(numbers) 
