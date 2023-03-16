# Program features :
# *Accepts a number from the user and checks whether it is divisible by 3 AND 7.
# *Displays a proper message if it is divisible.


# Title

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
           *program to check divisibilty by 3 and 7                                                 
''')

# Define the main function.

def div(x):
    x = int(x) # convert string parameter to integer
    if x%3==0: # if remainder 0
        if x%7==0: # if remainder also 0 
            return True # Then true
            
    else:
        return False # maybe False
        
# The Loop

while True:        # continues loop repeatedly
    num = input("Enter the number you want to check for the divisibility (enter '0' to exit program)..: ") # takes the input
    if num=="0":
        break # exits program if input is = 0
    
    if div(num): # function is called
        print("{0} is divisible by both 3 and 7".format(num)) # output
    
    else:
        print("{0} is not divisible by both 3 and 7".format(num)) # output #2