# This file explains what to do to implement new functionalities that have been discussed in the report

# Accuracy of direct 
One of the issues raised by the customer is that the directs are difficul to be understood. 
In some cases, the name of the beacon has to be said letter by letter (eg: "AMB" has to be pronounced "Alpha Mike Bravo") whereas others have to be said as word ("PERIG" has to be pronounced "PERIG" or "Périg").
To be able to implement a solution where each word is pronounced the way the customer wants, several things have to be done:
	
`1.` In the file `beacons.py`, modify the dictionary and add all the associations of beacons_name/prononciation in the dictionary

`2.` In the file `reading.py`, call the method direct_precise instead of direct from the file `say_direct.py`
	
To read the direct, the application will read the prononciation of each beacon as written in the dictionary.
By default, if the beacon's name is not present in the dictionary, the application will read the name letter by letter transforming each letter in the aeronautical alphaet.

# Restricted callsign

One of the issues raised by the customer is the fact that in some cases, the callsign said by the pilot during the readback corresponds only to the second part of the callsign.

For example, AFR12E4 would only readback "unit two echo 4" rather than "Air France unit two echo 4".
To do so, you can simply return: tr.transform_numbers(tr.transform_letters(rest,language,proba_error),language,proba_error,False) in the `say_callsign` method
This is considering that the three first letters always correspond to the airline in the callsign given.

NB. This functionality could also be put in place as an optionnal parameter that the customer can turn on and off. If this is what you wish to do, reuse what has been done for the errors (-e) to implement a similar functionality.

# First contact

One of the issues raised by the customer is the fact that in certain cases, it can be useful to not only be able to deliver a readback but also for a pilot to contact first the air traffic controller.
This was not in the context of our application but if it has to be implemented, here is how it could be done

`1. ` Add a field "first contact" in the JSON files that arrive: its value is a boolean

`2. ` In the file `reading.py`, in the function create_sentence , uncomment the commented line

`3. ` Add a parameter to the "fields" method.

`4. ` Create new functions call "say_heading_first_contact", "say_level_first_contact", ect. that say thos informations when it is a first_contact.

`5. ` Create with these functions in the "fields" method and the create_sentence method a new sentence. Use an if/else that call the different functions whether it is a first contact or not.

