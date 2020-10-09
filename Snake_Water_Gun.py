import random

def game(comp,you):

    if comp==you:
        return None

    elif comp=='w':
        if you=='g':
            return False
        elif you=='s':
            return True

    elif comp=='g':
        if you=='s':
            return False
        elif you=='w':
            return True

    elif comp=='s':
        if you=='w':
            return False
        elif you=='g':
            return True

print("Computer Turn: Snake(s), Water(w), Gun(g)?")
val = random.randint(1,3)

if val==1:
    comp = 's'
elif val==2:
    comp = 'w'
elif val==3:
    comp = 'g'

you = input("Your Turn: Snake(s), Water(w), Gun(g)?")

ans = game(comp,you)
print(f"Computer choose {comp}")
print(f"You choose {you}")
if ans==None:
    print("Game is a tie")
elif ans:
    print("You Win the game")
else:
    print("Computer win the game")

