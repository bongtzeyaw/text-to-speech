import transformations as tr

# Function that returns a sentence depending on the value of the level in the JSON file
def level(level,language,proba_error):
    fl_type = level["type"]
    value = tr.transform_numbers(level["valeur"],language,proba_error)

    if language == "FR":
        switcher_level_FR = {
            "descente"  : "Descendons niveau {}. . ".format(value),
            "montee"    : "Mon tons niveau {}. .".format(value),
            "fixe"      : "Maintenons niveau {}. . ".format(value),
        }
        return switcher_level_FR[fl_type] 
    elif language == "EN":
        switcher_level_EN = {
            "descente"  : "Descending level {}. . ".format(value),
            "montee"    : "Climbing level {}. . ".format(value),
            "fixe"      : "Maintaining level {}. . ".format(value),
        }
        return switcher_level_EN[fl_type] 