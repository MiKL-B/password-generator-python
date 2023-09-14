import random
import string
import os
import sys
from sys import platform


class App:
    def __init__(self):
        pass


    def main(self):
        self.display_menu()


    def display_title(self):
        os.system("title Password-generator - Python")
        print("Welcome in the Password-generator - Python")


    def display_menu(self):
        self.clear_console()
        self.display_title()
        print()

        choice_letter = None
        while choice_letter is None:
            try:
                choice_letter = int(input(f"Choose how many letters you want: "))
            except ValueError:
                print("Invalid integer!")

        choice_character = None
        while choice_character is None:
            try:
                choice_character = int(input(f"Choose how many special characters you want: "))
            except ValueError:
                print("Invalid integer!")

        choice_digit = None
        while choice_digit is None:
            try:
                choice_digit = int(input(f"Choose how many digits you want: "))
            except ValueError:
                print("Invalid integer!")

        self.create_password(choice_letter,choice_character,choice_digit)



    def create_password(self,len_letter, len_character, len_digit):
        strings = random.sample(string.ascii_letters, len_letter)

        digits = []
        for i in range(len_digit):
            digits.append(str(random.randint(1,100)))

        characters = []
        for i in range(len_character):
            characters.append(random.choice('!"$%&#()*+,-.:¤;<=>?@[]^_`{|}~'))

        password = strings + digits + characters

        random.shuffle(password)
        print()
        print("Your password: ",''.join(password))



    # functions miscellaneous

    def clear_console(self):
        if platform == "linux":  # Linux
            os.system("clear")
        elif platform == "darwin":  # Mac
            os.system("clear")
        elif platform == "win32":  # Windows
            os.system("cls")

