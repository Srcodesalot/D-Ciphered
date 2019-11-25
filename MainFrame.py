import Writer
import Reciver
import time
import sys
import random

#ADD YOUR GMAIL CREDENTIALS HERE!
userName = "YourGmail@gmail.com"
key = "YourGmailPassword"

def open():
    display("     ≈≈ WELCOME TO ≈≈    ")
    print("")
    display("    ≈≈  D-CIPHERED!  ≈≈    ")
    print("")

    command = ''
    while command != "exit":
        print("•")
        print("-To create an Encrypted message type 'create' ")
        print("•")
        print("-To Decrypt a message type 'read' ")
        print("•")
        print("-Finally, To exit type 'exit'\n")
        command = input(">")
        if "create" in command.casefold():
            Writer.new(userName,key)

        elif "read" in command.casefold():
            Reciver.mailQueue(userName, key)
            decrypt = Reciver.decipher()
            display(decrypt)
#           time.sleep(len(decrypt)/4)        ///uncomment this string to add time to the display of your messages
            print("\n")
            con = input("when finished reading type anything to continue \n >")

        elif "exit" in command.casefold():
            sys.exit(0)
        else:
            print("im sorry that doesnt seem to be a command.")


def display(decrypt):
    target = decrypt
    targetA = list(target)
    guessA = [''] * len(targetA)

    x = 0
    while guessA != targetA:
        i = 0
        guess = ''
        while i < len(guessA):
            if guessA[i] == targetA[i]:
                pointless = 0
            else:
                guessA[i] = random.choice("≈~1234567890-=qwertyuiop[]\ asdfghjkl;'zxcvbnm,./!@#$%^&*()+QWERTYUIOP{}|ASDFGHJKL:ZXCVBNM<>?")
            guess += guessA[i]
            i += 1

        sys.stdout.write(f'\r{guess}')
        sys.stdout.flush()
        time.sleep(0.009)


open()