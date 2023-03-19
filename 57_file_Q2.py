#The game() function in a program lets a user play a game and returns the score as an integer. You need read a file "hi_score.txt"which is either blank 
#or contains the previous hi-score you need to write a program to update the hi_score whenever game() breaks the hi-score
def game():
    return 69

score = game()

with open ("hi_score.txt") as f:
    hi_score = f.read()

if (int(hi_score) < (score)):
    with open ("hi_score.txt",'w') as f:
        f.write(str(score))#write takes only str type and only one argument or we can use it as no arguments

elif (hi_score) == '':
    with open ("hi_score.txt",'w') as f:
        f.write(str(score))


