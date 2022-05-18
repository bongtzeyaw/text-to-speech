import os
from voxpopuli import Voice
import pickle5
import numpy as np
import sys
sys.path.insert(1, 'Code/build_sentence/')
import reading
sys.path.insert(1, 'Code/speak/')
import sentence_vp


class Session():

    def __init__(self, voices_FR, voices_EN,file_to_read,load,dic_to_load,save,dic_to_save,speak,save_file,save_file_name,insert_error,language):
        self.dico_pilote = {}
        self.nb_pilotes = 0
        self.ind_voice_FR= 0
        self.ind_voice_EN = 0
        self.load=load
        self.dic_to_load=dic_to_load
        if (self.load):
            self.dico_pilote = self.load_session(self.dic_to_load)
            for (key,value) in self.dico_pilote.items():
                if value["lang"]=="fr":
                    self.ind_voice_FR+=1
                elif value["lang"]=="en" or value["lang"]=="us":
                    self.ind_voice_EN+=1
        self.voices_FR = voices_FR
        self.voices_EN = voices_EN
        self.nb_voices_FR = len(self.voices_FR)
        self.nb_voices_EN = len(self.voices_EN)
        self.file_to_read=file_to_read
        self.save=save
        self.dic_to_save=dic_to_save
        self.speak=speak
        self.save_file=save_file
        self.save_file_name=save_file_name
        self.insert_error=insert_error
        self.language=language

    # Function creates voice with different parameters
    def create_voice(self,voice):
        return (Voice(lang=voice["lang"], pitch =voice["pitch"], speed = voice["speed"], volume=voice["volume"], voice_id= voice["voice_id"]))

    # Function that calls speak_sentence
    def receive_data(self, json_file):
        language,sentence,indicatif = reading.create_sentence(json_file,self.insert_error,self.language)
        if not (indicatif in self.dico_pilote):
            if language == "FR":
                self.dico_pilote[indicatif] = self.voices_FR[self.ind_voice_FR]
                self.ind_voice_FR = (self.ind_voice_FR +1) % self.nb_voices_FR

            elif language == "EN":
                self.dico_pilote[indicatif] = self.voices_EN[self.ind_voice_EN]
                self.ind_voice_EN = (self.ind_voice_EN +1) % self.nb_voices_EN
        voice=self.create_voice(self.dico_pilote[indicatif])
        sentence_vp.speak_sentence(voice,sentence,self.speak,self.save_file,self.save_file_name)
        

    def load_session(self,dic):
        return pickle5.load(open(dic+".p", "rb"))

    def save_session(self,dic):
        pickle5.dump(dic, open(self.dic_to_save+".p","wb"))

    def run(self):
        
        json_file = "Code/Testing/" + self.file_to_read + ".json"
        if os.path.isfile(json_file):
            self.receive_data(json_file)

        else:
                print("Chemin d'accès du fichier à lire introuvable, veuillez réessayer")
        if self.save:
            self.save_session(self.dico_pilote)