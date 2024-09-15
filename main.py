import random
from colorama import *

banner = """
  _                                   
 / \   _|_ |_   _   _  |_   _   _ _|_ 
 \_/ >< |_ | | (/_ (_| | | (_) _>  |_ 
                    _|                               
"""

dico = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def main(alphabet):
    print(Fore.LIGHTRED_EX)
    print(banner)
    alpha = alphabet.copy()
    random.shuffle(alpha)
    print(Fore.BLUE)
    print("Dictionary Encrypt : ")
    print({alphabet[i]: alpha[i] for i in range(len(alphabet))})

main(dico)
print(Fore.RESET)