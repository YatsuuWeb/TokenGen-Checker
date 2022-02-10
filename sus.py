import random
from colored import fg
import sys
from time import sleep
import time
import os
from os import system,name, write
from requests import get, post
from random import randint
from pystyle import *

os.system("start paix.mp3")

def clear():
    system('nt' if name == "clear" else "cls")

if name == 'nt':
    system("title TokenGen & mode 120,30")

caracteres = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
gencode = ""
code = ""
bb = ""

def typewritter(text):
    for x in text:
        print(x, end="")
        sys.stdout.flush()
        sleep(0.1)




def checker():
    print(f"""{fg(47)}

 _______  _____  _     _ _______ __   _      _______ _     _ _______ _______ _     _ _______  ______
    |    |     | |____/  |______ | \  |      |       |_____| |______ |       |____/  |______ |_____/
    |    |_____| |    \_ |______ |  \_|      |_____  |     | |______ |_____  |    \_ |______ |    \_
                                                                                                    

    """)
    def variant1(token):
        response = get('https://discord.com/api/v6/auth/login', headers={"Authorization": token})#Bad variant for mass token check due to the rate limit.
        return True if response.status_code == 200 else False
    def variant2(token):
        response = post(f'https://discord.com/api/v6/invite/{randint(1,9999999)}', headers={'Authorization': token})
        if "You need to verify your account in order to perform this action." in str(response.content) or "401: Unauthorized" in str(response.content):
            return False
        else:
            return True
    def variant2_Status(token):
        response = post(f'https://discord.com/api/v6/invite/{randint(1,9999999)}', headers={'Authorization': token})
        if response.status_code == 401:
            return 'Invalid'
        elif "You need to verify your account in order to perform this action." in str(response.content):
            return 'Phone Lock'
        else:
            return 'Valid'
            
    if __name__ == "__main__":
        try:
            checked = []
            with open('tokens.txt', 'r') as tokens:
                for token in tokens.read().split('\n'):
                    if len(token) > 15 and token not in checked and variant2(token) == True:
                        print(f'{fg(8)}Token {fg(9)}{token} is Valid')
                        checked.append(token)
                    else:
                        print(f'{fg(8)}Token {fg(8)}{token} is Invalid')
            if len(checked) > 0:
                save = input(f'{len(checked)} valid tokens\nSave to File (y/n)').lower()
                if save == 'y':
                    name = randint(100000000, 9999999999)
                    with open(f'{name}.txt', 'w') as saveFile:
                        saveFile.write('\n'.join(checked))
                    print(f'Tokens Save To {name}.txt File!')
            input('Press Enter For Exit...')
        except:
            input('Can`t Open "tokens.txt" File!')



def tokennn():
    print(f"""{fg(93)}
    
 @@@@@@@  @@@@@@  @@@  @@@ @@@@@@@@ @@@  @@@       @@@@@@@  @@@@@@@@ @@@  @@@
   @@!   @@!  @@@ @@!  !@@ @@!      @@!@!@@@      !@@       @@!      @@!@!@@@
   @!!   @!@  !@! @!@@!@!  @!!!:!   @!@@!!@!      !@! @!@!@ @!!!:!   @!@@!!@!
   !!:   !!:  !!! !!: :!!  !!:      !!:  !!!      :!!   !!: !!:      !!:  !!!
    :     : :. :   :   ::: : :: ::: ::    :        :: :: :  : :: ::: ::    : 
                                                                             

    """)
    fileee=typewritter(input(f"{fg(8)}Enter for Gen token [{fg(93)}>{fg(8)}] ")) 
    while True:
        bb = ""
        gencode = ""
        code = ""
        for i in range(27):bb = f'{bb}{random.choice(caracteres)}'
        for i in range(6):
            code = f'{code}{random.choice(caracteres)}'
        print(f'{fg(8)}[+] {fg(93)}N{gencode}.{code}.{bb}\n')
        for i in range (23):
            gencode = f'{gencode}{random.choice(caracteres)}'
        print(f'{fg(8)}[+] {fg(93)}N{gencode}.{code}.{bb}\n')

        with open("tokens.txt", 'a+') as gen:
            gen.write(f"N{gencode}.{code}.{bb}\n")
            gen.write(f"O{gencode}.{code}.{bb}\n")
            gen.close()


class Main():
    def __init__(self):
        self.gg = True
        self.r = '\033[31m'
        self.g = '\033[32m'
        self.y = '\033[33m'
        self.b = '\033[34m'
        self.m = '\033[35m'
        self.c = '\033[36m'
        self.w = '\033[37m'
        self.rr = '\033[39m'
        self.cls()
        self.start_logo()
        self.options()
        while self.gg == True:
            choose = input(str(f'{fg(9)}  >  '))
            if(choose == str(1)):
                os.system("cls")
                tokennn()
            elif(choose == str(2)):
                os.system("cls")
                
                self.cls()
                checker()


    def cls(self):
        linux = 'clear'
        windows = 'cls'
        os.system([linux, windows][os.name == 'nt'])

    def start_logo(self):
        clear = "\x1b[0m"
        colors = [1]

        x = f"""
                                           {fg(9)}▄████████ ███    █▄     ▄████████ 
                                          {fg(9)}███    ███ ███    ███   ███    ███ 
                                          {fg(9)}███    █▀  ███    ███   ███    █▀  
                                          {fg(9)}███        ███    ███   ███        
                                        {fg(9)}▀███████████ ███    ███ ▀███████████ 
                                                 {fg(9)}███ ███    ███          ███ 
                                           {fg(9)}▄█    ███ ███    ███    ▄█    ███ 
                                          {fg(9)}▄████████▀  ████████▀   ▄████████▀  
        """

        for N, line in enumerate(x.split("\n")):
            sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
            time.sleep(0.05)

    def options(self):
        print(f'{fg(8)}[{fg(9)}1{fg(8)}] Token Gen')
        print(f'{fg(8)}[{fg(9)}2{fg(8)}] Checker Token\n')


Main()

