from emoji import emojize

def main():
    try:
        user_input = input("Input: ")
        get_emoji(user_input)
    except ValueError:
        return

def get_emoji(txt_input):
    print("Output: ",emojize(txt_input,language='alias'))


main()
