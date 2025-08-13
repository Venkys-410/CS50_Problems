import random


def main():

    lvl = get_level()
    
    
    ques = 10
    score = 0
    while ques > 0:
         x = generate_integer(lvl)
         y = generate_integer(lvl)
         #print(x,y)
         chances = 3
         while chances > 0:
            try:
                ans = int(input(f"{x} + {y} = "))
                if ans != (x+y):
                    chances -= 1
                    print("EEE")
                else:
                    score+=1
                    ques-=1
                    break
                if chances == 0:
                    ques -= 1
                    print(f"{x} + {y} = {x+y}")
                    break
            except TypeError:
                chances -= 1

    print(f"Score: {score}")
            
   
    

def get_level():
    while True:
        try:
            lvl = int(input("Level: "))
            if lvl in [1,2,3]:
                return lvl
        except (ValueError,TypeError):
            continue
    ...


def generate_integer(level):
    if level == 1:
        return random.randint(0,9)
    elif level == 2:
        return random.randint(10,99)
    else:
        return random.randint(100,999)


if __name__ == "__main__":
    main()