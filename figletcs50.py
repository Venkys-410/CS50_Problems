from pyfiglet import Figlet
from random import choice
import sys

figlet = Figlet()

fontsList = figlet.getFonts()

# print(fontsList)

def main():
    arg_length = len(sys.argv)
    if arg_length == 1:
        font_style = choice(fontsList)
        get_user_input(font_type=font_style)
    elif arg_length != 3 or sys.argv[1] not in ['-f','--font'] or sys.argv[2] not in fontsList: 
        sys.exit('Invalid usage')
    else:
        get_user_input(font_type=sys.argv[2])

def get_user_input(font_type):
    user_text = input("Input: ")
    print(font_type)
    figlet.setFont(font=font_type)
    print(figlet.renderText(user_text))

main()