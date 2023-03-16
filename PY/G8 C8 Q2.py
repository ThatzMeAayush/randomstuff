# Funtion features :
# Accepts a string from the user.
# Displays the total number of vowels and consonants in it

print('''
                                                                    © Ayush Sahu *title by patorjk.com®™
 ██▓███   ██▀███   ▄▄▄       ▄████▄  ▄▄▄█████▓ ██▓ ▄████▄  ▓█████ 
▓██░  ██▒▓██ ▒ ██▒▒████▄    ▒██▀ ▀█  ▓  ██▒ ▓▒▓██▒▒██▀ ▀█  ▓█   ▀ 
▓██░ ██▓▒▓██ ░▄█ ▒▒██  ▀█▄  ▒▓█    ▄ ▒ ▓██░ ▒░▒██▒▒▓█    ▄ ▒███   
▒██▄█▓▒ ▒▒██▀▀█▄  ░██▄▄▄▄██ ▒▓▓▄ ▄██▒░ ▓██▓ ░ ░██░▒▓▓▄ ▄██▒▒▓█  ▄ 
▒██▒ ░  ░░██▓ ▒██▒ ▓█   ▓██▒▒ ▓███▀ ░  ▒██▒ ░ ░██░▒ ▓███▀ ░░▒████▒
▒▓▒░ ░  ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ░▒ ▒  ░  ▒ ░░   ░▓  ░ ░▒ ▒  ░░░ ▒░ ░
░▒ ░       ░▒ ░ ▒░  ▒   ▒▒ ░  ░  ▒       ░     ▒ ░  ░  ▒    ░ ░  ░
░░         ░░   ░   ░   ▒   ░          ░       ▒ ░░           ░   
            ░           ░  ░░ ░                ░  ░ ░         ░  ░
                            ░                     ░               
                                *program to find no. of consonant and vowels
                            ''')

def vowels_and_cons(string):
    
    vowels = ('a','e','i','o','u','A','E','I','O','U')
    v = 0
    c = 0
    for i in string:
        if i in vowels:
            v += 1
        elif i.isalpha():
            c += 1
    print("Vowels :", v)
    print("Consonants :", c)

while True:
    strin = input("Enter the word/sentence (Leave blank & press enter to exit)..: ")
    if strin=="":
        break
    vowels_and_cons(strin)

