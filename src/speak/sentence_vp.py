""" File containing functions to say a sentance using module voxpopuli """

import phonemes_processing as phon 
import pkg_resources
from ctypes import *
from contextlib import contextmanager
import pyaudio

ERROR_HANDLER_FUNC = CFUNCTYPE(None, c_char_p, c_int, c_char_p, c_int, c_char_p)

def py_error_handler(filename, line, function, err, fmt):
    pass

c_error_handler = ERROR_HANDLER_FUNC(py_error_handler)

# Enables to not show the ALSA errors due to pyaudio
@contextmanager
def noalsaerr():
    asound = cdll.LoadLibrary('libasound.so')
    asound.snd_lib_error_set_handler(c_error_handler)
    yield
    asound.snd_lib_error_set_handler(None)

# Speaks or saves the file depending on the user's input
def speak_sentence(voice, sentence,speak,save_file,save_file_name):
    phonemes = phon.create_phonemes(voice, sentence)
    if (speak): # if the user had decided to make the system speeak
        with noalsaerr():
            voice.say(phonemes)
    wav = voice.to_audio(phonemes)
    
    if (save_file): # if the user has decided to save the file, the file is saved with the name given by the user
        with open(save_file_name+".wav","wb") as wavfile:
            wavfile.write(wav)
    return None


   

    