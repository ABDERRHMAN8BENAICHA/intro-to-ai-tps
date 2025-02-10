try : 
    c = int(input("Enter a celsius temperature: "))
    c = c*(9/5)+32
    print(f"{c:.2f} F")
except ValueError :
    print("Invalid input. Please enter a valid number")





# Test Cases:
# ---------------------------------------------------------------
# | Input (Celsius) | Output (Fahrenheit)                       |
# |-----------------|-------------------------------------------|
# | 0              | 32.0 F                                     |
# | 100            | 212.0 F (Boiling point of water)           | 
# | -40            | -40.0 F (Same in both scales)              |
# | 37             | 98.6 F (Body temperature)                  |
# | abc            | Invalid input. Please enter a valid number.|
# ---------------------------------------------------------------