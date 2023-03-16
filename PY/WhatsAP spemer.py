# © Ayush Sahu
import pyautogui as pt
import time

print('''
                                                        © Ayush Sahu *title by patorjk.com®™
  ██████  ██▓███  ▓█████  ███▄ ▄███▓▓█████  ██▀███  
▒██    ▒ ▓██░  ██▒▓█   ▀ ▓██▒▀█▀ ██▒▓█   ▀ ▓██ ▒ ██▒
░ ▓██▄   ▓██░ ██▓▒▒███   ▓██    ▓██░▒███   ▓██ ░▄█ ▒
  ▒   ██▒▒██▄█▓▒ ▒▒▓█  ▄ ▒██    ▒██ ▒▓█  ▄ ▒██▀▀█▄  
▒██████▒▒▒██▒ ░  ░░▒████▒▒██▒   ░██▒░▒████▒░██▓ ▒██▒
▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░░░ ▒░ ░░ ▒░   ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░
░ ░▒  ░ ░░▒ ░      ░ ░  ░░  ░      ░ ░ ░  ░  ░▒ ░ ▒░
░  ░  ░  ░░          ░   ░      ░      ░     ░░   ░ 
      ░              ░  ░       ░      ░  ░   ░     
                                                    
''')
limit = input("Enter limit:")
message = input("Enter message:")
i = 0
time.sleep(5)

while i <= int(limit):
    pt.typewrite(message)     

    pt.press("enter")

    i+=1
