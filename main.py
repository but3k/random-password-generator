import random
import string
import os
import time

print("Random password generator")

use_digits = input("Add numbers? (y/n) ").lower() == 'y'
use_symbols = input("Add symbols? (y/n) ").lower() == 'y'

chars = string.ascii_lowercase
if use_digits:
    chars += string.digits
if use_symbols:
    chars += string.punctuation    

lenght = int(input("How long does your password need to be? "))
password = ''.join(random.choice(chars) for _ in range(lenght))

print("Your password is " + password)
input("Press enter to exit...")