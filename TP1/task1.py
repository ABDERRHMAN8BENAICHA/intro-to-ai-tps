try:
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")
except ValueError:
    print("Invalid input. Please enter a valid number.")





# Test Cases:
# ------------------------------------------------------
# | Input  | Expected Output                            |
# |--------|--------------------------------------------|
# | 4      | Even                                       |
# | 7      | Odd                                        |
# | 0      | Even                                       |
# | -2     | Even                                       |
# | -3     | Odd                                        |
# | 100    | Even                                       |
# | 999    | Odd                                        |
# | abc    | Invalid input. Please enter a valid number |
# -------------------------------------------------------
