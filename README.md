# text-to-speech
A project of Python Programming that generates a speech (pilot read-back) from a given text (information or instruction from air traffic controller). The goal is that the output speech will satisfy a number of KPIs and adhere to the Aviation Phraseology requirements set by the French Aeronautical Information Service (SIA).

# Installation of the project

This project requires `python3` to work. For the different packages, package manager `pip3` is also required.

First, make sure `espeak` is installed:

```
sudo apt-get install espeak
```

To install MBROLA with voices, run the associated file with : 

```
python3 install_mbrola.py
```
This will install MBROLA, the 7 french voices and the 4 english voices (3 `us` and 1 `en`).


MBROLA can also be installed manually by typing and runnning in a terminal : 

```
sudo apt-get update

sudo apt-get install mbrola


```

To install voices manually, run : 
```
sudo apt install mbrola-fr1
```
This will install the first french voice. Other voices can be installed by typing the same command as above and replacing `fr1` with another voice identifier.
See [mbrola voices database](https://github.com/numediart/MBROLA-voices/tree/master/data) for more details about the indicatives.

Then, install the python packages necessary for the project with : 

```
pip3 install -r requirements.txt
```

The application is now ready to run!

To run it:

```
python3 main_session.py -h
```

This will give you all the information you need on which parameters to put while launching the application.
If you wish to see a quick demonstration of everything that can be done, you can open [Demo.md] and run the successive files.

NB. Depending on the machine/virtual machine and Linux distribution you use, you might have some issues with the application. 
In fact, the import of files from a folder to another do not always work. If that it the case :

**1.** In the file "session.py", modify :

```
import sys
sys.path.insert(1, 'build_sentence/')
import reading
sys.path.insert(1, 'speak/')
import sentence_vp
```

to :

```
import sys
sys.path.insert(1, 'Code/build_sentence/')
import reading
sys.path.insert(1, 'Code/speak/')
import sentence_vp
```

**2.** In the function run of the same file, modify:

```
	json_file = "Testing/" + self.file_to_read + ".json"
```

to :

```
	json_file = "Code/Testing/" + self.file_to_read + ".json"

```

**3.** In the function main of the file "main_session.py", towards the end, modify:

```
    french_voices,english_voices=generate_lists("voices.json")

```

to:

```
    french_voices,english_voices=generate_lists("Code/voices.json")
```


