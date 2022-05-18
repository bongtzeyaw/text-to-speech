import alphabets as dic
import random


# This function receives a string that will represent the plane id
# The language also is necessary to decide what dictionary that translated letters in aeronautical letters is used.
# It returns a string with the aeronautic pronounciation representing the same plane id 
# Example : "AFRHW" is transformed into "alpha foxtrot romeo hotel whisky" """
# There is the possibility to add a mistake with a probability of proba_error.
# In this case the letters are not translated
def transform_letters(string,language,proba_error):
    
    result = ""
    dic_use=""
    no_mistake_insert=(proba_error==None)
    # No insertion of random mistake
    if not no_mistake_insert:
         error = random.random() < proba_error  # A mistake resultst in not splitting the digits in a number 
    if no_mistake_insert or (not error):
        if language=="FR":
            dic_use=dic.DIC_LETTERS_FR
        else:
            dic_use=dic.DIC_LETTERS_EN
        for caractere in string:
            try:
                result += dic_use[caractere]+", "  
            except KeyError:
                result+=caractere+", " 
        
    else:
        for caractere in string:
            result+=caractere+", "
    return result[:-1]

# This function receives a string of numbers and translates it
# It also needs the language to translate "1" to "unit" or "unité"
# It returns a string of the same numbers but each digit is spaced out and '1' is replaced with unit or unité
# Example : "1234" is transformed into "unit 2 3 4" or "unité 2 3 4"
def transform_numbers(string,language,proba_error,div_hundred=True): 
    if div_hundred and float(string)%100==0:
        return string
    result = ""
    no_mistake_insert=(proba_error==None)
    # No insertion of random mistake
    if not no_mistake_insert:
        error = random.random() < proba_error

    if no_mistake_insert or (not error):
        for digit in string:
            if digit.isnumeric():
                if digit == '1':
                    if language == "FR":
                        result += " unité "
                    if language == "EN":
                        result += " unit " 
                elif digit == '8':
                    if language == "FR":
                        result += " huite "
                    else: result+=" 8 "
                else:
                    result += digit 
                    result += " "
            elif digit == '.':
                if language == "FR":
                    result += " décimale "
                if language == "EN":
                    result += " decimal "
            else:
                result+=digit
    # Insertion of a mistake with a probability value of proba_error
    else:
        for digit in string:
            if digit == '.':
                if language == "FR":
                    result += " décimale "
                if language == "EN":
                    result += " decimal "
            else:
                result+=digit
        result+=" "
    return result[:-1]