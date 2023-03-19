import random

def game(comp,you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp == 'w':
        if you == 's':
            return True
        elif you == 'g':
            return False
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True

print("Comp Turn:Snak(s) Water(w) or Gun(g)?")
randno = random.randint(1,3)#by importing random we get randint function to use
if randno == 1:
    comp == 's'
elif randno == 2:
    comp == 'w'
elif randno == 3:
    comp == 'g'

you= input("Your Turn:Snake(s) Water(w) or Gun(g)?")#####incomplete  game


a = game(comp,you)
print(a)

print(f"Computer chosen: {comp}")
print(f"you chosen: {you}")

if a == None:
    print("The game is a tie!")
elif a:
    print("You win!")
elif a:
    print("You lose!")

#incomplette