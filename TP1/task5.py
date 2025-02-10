while True:
    try:
        text = input("Enter a word: ").strip()
        
        if len(text) < 2:
            print("Text must have at least two characters.")
            continue
        
        result = list(text) 
        result[0], result[-1] = text[-1].upper(), text[0].lower()  
        result = "".join(result)  

        print("Original Text:", text)
        print("Edited Text:", result)
        break

    except Exception as e:
        print("An error occurred:", e)






# Test Cases:
# ---------------------------------------------------------------------------------------------------
# | Input (Text)      | Original Text                  | Expected Output (Edit Text)                |
# |-------------------|--------------------------------|--------------------------------------------|
# | "hello"           | hello                          | Oellh                                      |
# | "python"          | python                         | Nythop                                     |
# | "Hi"              | Hi                             | Ih                                         |
# | "A"               | A                              | Text must have at least two characters.    |
# | ""                | ""                             | Text must have at least two characters.    |
# ---------------------------------------------------------------------------------------------------  
