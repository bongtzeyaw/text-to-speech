import session
from voxpopuli import Voice
from generate_lists import generate_lists
import argparse

# Main function that calls the session and enables the user to define what he wants to do
def __main__():
    # Creation of the parser that will enable the user to define what he wants to do
    parser = argparse.ArgumentParser()
    save_dic = parser.add_mutually_exclusive_group()
    language = parser.add_mutually_exclusive_group()
    # Argument of the application: JSON file to be treated and readback
    parser.add_argument("file_to_read", type=str,
                     help="JSON file to be read by the application")
    
    # Possibility to impose the language in which the file is read no matter what the language defined in the JSON file is
    language.add_argument("-fr", "--french", help="impose a french pilot",
                    action="store_true")
    language.add_argument("-en", "--english", help="impose an english pilot",
                    action="store_true")
    
    # Possibility to load an already existing session 
    parser.add_argument("-l", "--load_session", type=str, default="", metavar=" Session name",
                    help="load an already existing session that associates callsigns and voices")
    
    # Application will speak and read the readback
    parser.add_argument("-nsp", "--do_not_speak", help="do not say the corresponding clearance",
                    action="store_false")
   
    # Application will save the audio file with the name specified by the user
    parser.add_argument("-sf", "--save_file", type=str, default="", metavar=" Audio file name",
                    help="save the audio file under a specific name")
    
    # Application will save the session with the JSON file just treated and with a new name
    save_dic.add_argument("-ss", "--save_session", type=str, default="", metavar=" Session to save name",
                    help="save the new session with a new name")
    
    # Application will save the session with the JSON file just treated keeping the same name that the loaded file
    save_dic.add_argument("-lss", "--load_save_session", type=str, default="", metavar=" Session to load and save name",
                    help="load a session and save it with the new clearance")
    # Possibility for the user to insert a probability of error for the readback to be mis-said
    parser.add_argument("-e", "--insert_error", type=float, 
                    help="add a volontary error with a particular probability")  
    
    args = parser.parse_args()
    load=True
    save_dic=True
    save_file=True
    dic_to_save=args.save_session
    dic_to_load=args.load_session
    language=""
    if ((args.load_session=="" or args.load_session==None) and (args.load_save_session=="" or args.load_save_session==None)): # if no session has been entered, no session is to be loaded
        load=False
    if (args.load_save_session!="" and args.load_save_session!=None):
            dic_to_save=args.load_save_session
            dic_to_load=args.load_save_session
    if ((args.save_session=="" or args.save_session==None) and (args.load_save_session=="" or args.load_save_session==None)):
        save_dic=False
    if (args.save_file=="" or args.save_file==None):
        save_file=False

    if (args.french):
        language="FR"
    if (args.english):
        language="EN"

    french_voices,english_voices=generate_lists("Code/voices.json")
    
    ses = session.Session(french_voices, english_voices, args.file_to_read,load,dic_to_load,save_dic,dic_to_save, args.do_not_speak,save_file,args.save_file,args.insert_error,language)
    ses.run()

__main__()    
