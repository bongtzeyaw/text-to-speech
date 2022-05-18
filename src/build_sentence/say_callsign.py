
import transformations as tr
import companies as dic_compa

# This function writes the callsign: for example AFR23W is written "Air France 2 3 Whiskey" in english
# With a probability of proba_error, the callsign is not pronounced correctly
def callsign(callsign,language,proba_error):
    company=""
    rest=""
    for i in range(3):
        company+=callsign[i] # the three first letters of the callsign is always dedicated to the company
    for i in range(3,len(callsign)):
        rest+=callsign[i] # stores the rest of the callsign not corresponding to the company
    try:
        company_full_name=dic_compa.DIC_COMPANIES_CALLSIGN[company] # transforms AFR to Air France
        if company_full_name=="": # if the company was found in the DIC_COMPANIES_CALLSIGN dictionary but not associated to a full name
                callsign = tr.transform_numbers(tr.transform_letters(callsign,language,proba_error),language,proba_error,False) # the callsign is transformed to aeronautical language with its letters and numbers
        else:
            callsign=company_full_name+", "+tr.transform_numbers(tr.transform_letters(rest,language,proba_error),language,proba_error,False) # juxtaposing the name of the companie
    except KeyError: # if the company was not found in the DIC_COMPANIES_CALLSIGN dictionary
        callsign = tr.transform_numbers(tr.transform_letters(callsign,language,proba_error),language,proba_error,False) # the callsign is transformed to aeronautical language with its letters and numbers
    return "{}. . ".format(callsign)