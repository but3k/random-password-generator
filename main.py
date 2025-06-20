import random
import string
from colorama import init, Fore, Style
import os
import time

#First methods
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def loading_animation(message="Generating...", dots=3, delay=0.5):
    for i in range(dots):
        print(f"{Fore.CYAN}{message}{'.' * (i+1)}", end= '\r')
        time.sleep(delay)
    clear_screen

#Generator
def generate_password(lenght):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(lenght))

clear_screen
print(f"{Fore.YELLOW} Welcome in RPG (Random Password Generator) \n")

try:
    length = int(input(f"{Fore.GREEN} Enter password lenght: "))
    print()
    loading_animation()
    password = generate_password(length)
    print(f"{Fore.MAGENTA} Your password is: \n\n{Fore.WHITE + Style.BRIGHT}{password}\n")
except ValueError:
    print(f"{Fore.RED} Please enter valid number!") 