import transformations as tr

# This function returns the readback for a clearance of frequency change
def frequency(frequency,language,error):
    centre = frequency["centre"] #Note: Pas besoin de faire transform lettres (centres)
    value = tr.transform_numbers(frequency["valeur"],language,error)
    sentence = "{}, {}, ".format(centre, value)
    if language == "FR" : 
        sentence += "au revoir. . " # The plane is leaving a sector
    elif language == "EN" : 
        sentence += "good day. . "
    return sentence
     