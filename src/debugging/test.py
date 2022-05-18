from voxpopuli import Voice, FrenchPhonemes, BritishEnglishPhonemes


        
        

def phonemes_to_file(voice, phrase, file_name):
        list_phonemes = voice.to_phonemes(phrase)
        for phoneme in list_phonemes:
                if voice.lang == "fr":
                        if phoneme.name in FrenchPhonemes.VOWELS:
                                phoneme.duration *= 1.75
                         
                        elif phoneme.name == "_":
                                phoneme.duration = 250
                        last_phoneme = list_phonemes[-5]
                        last_phoneme.duration /= 1.75
                elif voice.lang == "en" or voice.lang == "us":
                        
                        if phoneme.name in BritishEnglishPhonemes.VOWELS:
                                
                                phoneme.duration *= 1.75
                         
                        elif phoneme.name == "_":
                                phoneme.duration = 250
                                
                        last_phoneme = list_phonemes[-5]
                        last_phoneme.duration /= 1.75
                        
        wav = voice.to_audio(list_phonemes)
        voice.say(list_phonemes)

if __name__== "__main__":
        langue = "fr" # "en" "us"
        v_id = 1 # de 1 à 7 pour voix fr, 1 à 3 pour voix anglaises
        wpm = 140 # 130 pour voix en1
        pitch=55

        # Phrases françaises
        if langue =="fr":
                col1 = "Québec Romeo Sierra Tango uniforme Victor Ouisss ki X-ray Yénki Zouulou"
                col2 = "Rinsse unité 2 8  décimale 3 4, au revoir. Hop 7   4." # Rinssse pour Reims
                col3 = "Nouveau cap 0 8 9. Air France Hotel   X-rèè."
                col4 = "Descendons niveau 0 5 0. Réduisons 3 unité 0 noeuds. SOCOFER Romeo   éko   8"
                col5 = "Continuons cap 0 4. Vitesse mach 0  décimale 7 6 maximum. DIVI, AIR, Juliaite,  Mike. "
                col6 = "Nouveau cap 2 6 7. Mon tons niveau 2 6 0. Vitesse mach 0  décimale 8 maximum. BOL Tango   Uhniforme."
                col7 = "Augmentons mach 0  décimale 8 9. ERIXU GUERE NARAK. NATCHAIR Yénki   Mike."

                # Phrases anglaises
        else:

                col1 = "Zoolu"
        
        liste_col = col1

        for i in range(0,7):
                voice = Voice(lang=langue, pitch=pitch, speed=wpm, voice_id=v_id)
                file_name = "col_{}{}.wav".format(langue,v_id)
                phonemes_to_file(voice,liste_col , file_name)