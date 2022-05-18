import transformations as tr
import alphabets as dic

# Function that returns a sentence depending on the value of the heading in the JSON file
def speed(speed,language,proba_error):
    type_vit = speed["type"]
    value = tr.transform_numbers(speed["valeur"],language,proba_error)
    units = speed["unit"]  

    def speed_value_unit(value, unit):
        if unit == "mach":
            return "{} {}".format(unit, value) # if the speed is in Mach, we say Mach .78
        return "{} {}".format(value,unit) # else we say 270 knots

    if language == "FR":
        value_unit_FR = speed_value_unit(value, dic.DIC_TRAD_FR_EN[units])
        switcher_speed_FR = {
            "minimum"       : "Vitesse {} minimum. . ".format(value_unit_FR), 
            "maximum"       : "Vitesse {} maximum. . ".format(value_unit_FR), 
            "reduction"     : "Réduisons {}. . ".format(value_unit_FR),  
            "augmentation"  : "Augmentons {}. . ".format(value_unit_FR),  
            "indiquee"       : "{}. . ".format(value_unit_FR),  
        }
        return switcher_speed_FR[type_vit] 
    elif language == "EN":
        value_unit_EN = speed_value_unit(value, units)
        switcher_speed_EN= {
            "minimum"       : "Speed {} or greater. . ".format(value_unit_EN), 
            "maximum"       : "Speed {} or less. . ".format(value_unit_EN), 
            "reduction"     : "Reducing {}. . ".format(value_unit_EN),  
            "augmentation"  : "Increasing {}. . ".format(value_unit_EN),  
            "indiquee"       : "{}. . ".format(value_unit_EN),  
        }
        return switcher_speed_EN[type_vit] 
