import beacons as be
import transformations as tr
# This functions returns the readback of a clearance for direct
def direct(direct, language,proba_error):
    direct=direct.replace(" ",", ")
    return "{}. . ".format(direct) #Note: Does not depend on the language


def direct_precise(direct, language,proba_error):
    direct_list=direct.split()
    direct_said=""
    for word in direct_list:
        try:
            phonetic=be.BEACONS[word]
        except KeyError:
            phonetic=tr.transform_letters(word,language,proba_error)
        direct_said+=phonetic+", "
    return direct_said