import inflect

p = inflect.engine()

def main():
    name_list = []
    while True:
        try:
            name = input("Name: ")
            name_list.append(name)
        except EOFError:
            break
    say_adieu(name_list)

def say_adieu(names):
    print("Adieu, adieu, to",p.join(tuple(names)))



if __name__=='__main__':
    main()