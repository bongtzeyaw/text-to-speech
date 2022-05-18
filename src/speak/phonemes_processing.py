from voxpopuli import Voice, FrenchPhonemes, BritishEnglishPhonemes

""" This module converts a clearance into a list of phonemes that can be used with a mbrola voice """

# Converts a sentence into a list of phonemes with a given voice
def create_phonemes(voice, sentence):
    phonemes = voice.to_phonemes(sentence)
    if voice.lang == "fr":
        return modify_phonemes_duration_fr(phonemes)
    elif voice.lang == "en" or voice.lang == "us":
        return modify_phonemes_duration_en(phonemes)


# The next two functions modify the duration of phonemes by:
# 1. Increasing the duration of vowels by multiply it by constant d > 1 (1.75 as default value) 
# 2. Fixing the time of pause between two clearances (default value 500ms) 
# Returns the modified list of phonemes
def modify_phonemes_duration_fr(list_phonemes, d = 1.75, s=0.9):
    
    for phoneme in list_phonemes:
        if phoneme.name in FrenchPhonemes.VOWELS:
            phoneme.duration *= d
        
        # The phoneme "_" is a pause and either a comma or a dot is always represented by two consecutives "_"
        elif phoneme.name == "_":
            phoneme.duration=phoneme.duration*s
        # We don't modify the last phoneme, if it's a vowel, to make it not too weird for the listener
        # The last 4 phonemes of a sentence are always pauses ( i.e. 4 straght symbols "_") 
    last_phoneme = list_phonemes[-5]
    if last_phoneme.name in FrenchPhonemes.VOWELS:
        last_phoneme.duration /= d
    return list_phonemes

def modify_phonemes_duration_en(list_phonemes, d = 1.75, s=0.9):
    for phoneme in list_phonemes:
        if phoneme.name in BritishEnglishPhonemes.VOWELS:
            phoneme.duration *= d
        
        # The phoneme "_" is a pause and either a comma or a dot is always represented by two consecutives "_"
        elif phoneme.name == "_":
            phoneme.duration=phoneme.duration*s
        # We don't modify the last phoneme, if it's a vowel, to make it not too weird for the listener
        # The last 4 phonemes of a sentence are always pauses ( i.e. 4 straght symbols "_") 
    last_phoneme = list_phonemes[-5]
    if last_phoneme.name in BritishEnglishPhonemes.VOWELS:
        last_phoneme.duration /= d
    return list_phonemes





    


