try : 
    f = float(input("Enter a celsius temperature: "))
    f = (f-32)*(5/9)
    print(f"{f:.2f} C")
except ValueError :
    print("Invalid input. Please enter a valid number")





# Test Cases:
# -------------------------------------------------
# | Input (Fahrenheit) | Expected Output (Celsius) |
# |--------------------|--------------------------|
# | 32                | 0.0 C (Freezing point)     |
# | 212               | 100.0 C (Boiling point)   |
# | 98.6              | 37.0 C (Body temperature) |
# | -40               | -40.0 C (Same in both)    |
# | 0                 | -17.78 C                  |
# | abc               | Invalid input. Please enter a valid number |
# -------------------------------------------------
