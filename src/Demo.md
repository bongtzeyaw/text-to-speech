# This file will give you a quick demonstration of everything that can be made with the application

Firsty, you can see evey parameter running:
```
python3 main_session.py -h 
```

Let's say now that you want to read the file direct_level_FR and save the created session under the name session_1 (-ss session_1)

```
python3 main_session.py direct_level_FR -ss session_1
```



Now you want to read the file heading_speed_FR, using the same session that before and saving it afterwards (-lss session_1) with a readback error with a probability of 1 (-e 1).

```
python3 heading_speed_FR -lss session_1 -e 1
```
 
Now you want to just save the audio file level_FR without reading it out loud (-nsp), using the same session that before and saving it afterwards (-lss session_1). The audio file is to be saved with the name audio1 (-sf audio1).
The callsign in the file level_FR matches that of direct_level_FR so both readbacks will be done with the same voice.


```
python3 main_session.py level_FR -lss session_1 -nsp -sf audio1
```

Now you want to read the file heading_FR but forcing the use of english (-en), loading the session session_1 but not saving it after (-l)

```
python3 heading_level_speed_FR -l session_1 -en
```
