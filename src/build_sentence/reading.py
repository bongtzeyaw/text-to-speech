import json
import say_heading, say_direct,say_frequency,say_callsign,say_level,say_speed

# This function has as arguments: p, data, language and the probability of error, it works as a switcher and enables to create a sentence
def fields(p, data,language,proba_error):
        switcher ={
            "cap" : lambda : say_heading.heading(data["cap"],language,proba_error),
            "niveau": lambda : say_level.level(data["niveau"],language,proba_error),
            "vitesse": lambda : say_speed.speed(data["vitesse"],language,proba_error),
            "directe": lambda : say_direct.direct(data["directe"],language,proba_error),
            "frequence": lambda : say_frequency.frequency(data["frequence"],language,proba_error),
            "langage": lambda : "",
            "indicatif": lambda : "",
            "centre": lambda : ""
        }
        def raise_(p):
            raise p
        func = switcher.get(p, lambda : raise_(ValueError(p))) # raises an error if a value is mis entered in the original JSON file
        return func()

# This function has as arguments file_name: the name of a JSON file to say the clearance, the probability of returning the error and the language in which the sentence must be said
def create_sentence(file_name,proba_error,language):
    with open(file_name) as json_file:
        data = json.load(json_file)
        #first_contact=data["first_contact"] to be implemented later
        language_def = language if language!="" else data["langage"] # if the language is not specified by the user in the call of create_sentence, the language defined in the JSON file is used
        sentence = ""      
        for p in data:
            sentence += fields(p, data,language_def,proba_error) # appends together all the fields present in the JSON file by calling the function fields
        callsign = data["indicatif"]
        sentence += say_callsign.callsign(callsign,language_def,proba_error) # adding the callsign at the end of the sentence as the read-back of the clearance forces
    return (language_def,sentence, callsign)
