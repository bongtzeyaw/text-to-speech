import json
from voxpopuli import Voice

# This function reads the JSON file containing the list of the voices and creates two lists: one with the english voices and the other with the english ones
def generate_lists (filename):
    with open(filename) as json_data:
        french_voices=[]
        english_voices=[]
        data_dict = json.load(json_data)
        voice_number=0
        for key,value in data_dict.items():
            try:
                lang=value["lang"]
            except KeyError:
                lang="fr"
            try:
                pitch=int(value["pitch"])
            except KeyError:
                pitch=50
            try:
                speed=int(value["speed"])
            except KeyError:
                speed=140
            try: 
                volume=float(value["volume"])
            except KeyError:
                volume=1
            try:
                voice_id=int(value["voice_id"])
            except KeyError:
                voice_id=1
            if lang=='fr':
                french_voices.append({"voice_number":voice_number,"lang":lang, "pitch":pitch, "speed":speed, "volume":volume,"voice_id":voice_id})
            else : # ie if the language is english or us
                english_voices.append({"voice_number":voice_number,"lang":lang, "pitch":pitch, "speed":speed, "volume":volume,"voice_id":voice_id})
            voice_number+=1
        return (french_voices,english_voices)
