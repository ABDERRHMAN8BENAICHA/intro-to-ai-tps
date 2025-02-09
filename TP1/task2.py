while True:
    try:
        number = int(input("Enter a number between 1500 and 2700: "))
        
        if 1500 <= number <= 2700:
            if number % 7 == 0 and number % 5 == 0:
                print(f"{number} is divisible by 7 and a multiple of 5")
            else:
                print(f"{number} is not divisible by 7 and a multiple of 5")
            break  
        else:
            print("Number must be between 1500 and 2700. Try again.")
    except ValueError:
        print("Invalid input. Please enter a valid number")





# Test Cases:
# -----------------------------------------------------------
# | Input  | Expected Output                                  |
# |--------|------------------------------------------------|
# | 1500   | 1500 is not divisible by 7 and a multiple of 5 |
# | 1750   | 1750 is not divisible by 7 and a multiple of 5 |
# | 2100   | 2100 is divisible by 7 and a multiple of 5     |
# | 2700   | 2700 is not divisible by 7 and a multiple of 5 |
# | 1400   | Number must be between 1500 and 2700. Try again. |
# | 2800   | Number must be between 1500 and 2700. Try again. |
# | abc    | Invalid input. Please enter a valid number     |
# -----------------------------------------------------------