import transformations as tr
import alphabets as dic

# Function that returns a sentence depending on the value of the heading in the JSON file
def heading(heading,language,proba_error):
    heading_type = heading["type"]
    orient = heading["orientation"]
    value = tr.transform_numbers(heading["valeur"], language,proba_error,False) # transforming the value of the heading
    if language == "FR":
        switcher_heading_FR = {
            "absolu"    : "Nouveau cap {}. . ".format(value),
            "relatif"   : "Tournons à {} cap {}. . ".format(orient,value),
            "continu"  : "Continuons cap {}. . ".format(value),
        }
        return switcher_heading_FR[heading_type] 
    elif language == "EN":
        switcher_heading_EN = {
            "absolu"    : "New heading {}. . ".format(value),
            "relatif"   : "Turning {} heading {}. . ".format(dic.DIC_TRAD_FR_EN[orient],value),
            "continu"  : "Continuing heading {}. . ".format(value),
        }
        return switcher_heading_EN[heading_type]