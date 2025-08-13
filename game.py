from random import randint

'''
Prompts the user for a level,
. If the user does not input a positive integer, the program should prompt again.
Randomly generates an integer between 1 and n, inclusive, using the random module.
Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
If the guess is larger than that integer, the program should output Too large! and prompt the user again.
If the guess is the same as that integer, the program should output Just right! and exit.

'''

def main():
    while True:
        try:
            lvl = int(input("Level: "))
            if lvl < 0:
                raise ValueError()
            gen_rand(lvl)
            break
        except ValueError:
            continue

def gen_rand(n):
    ran_num = randint(1,n)
    get_guess(ran_num)

def get_guess(n):
    while True:
        try:
            guess = int(input("Guess: "))
            if guess < 0:
                raise ValueError()
            check_guess(guess,n)
            break
        except ValueError:
            continue

        
                              
def check_guess(g,n):
    if g < n:
        print("Too small!")
        get_guess(n)
    elif g > n:
        print("Too large!")
        get_guess(n)
    else:
        print("Just right!")
        return
    
main()
