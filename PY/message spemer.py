# © Ayush Sahu
import pyautogui as pt
import time

print('''
                                                        © Ayush Sahu
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
print('Program will now wait for 7 seconds till then open the messaging app...')
time.sleep(7)

while i <= int(limit):
    pt.typewrite(message)     

    pt.press("enter")

    i+=1
