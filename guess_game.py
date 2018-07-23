import random

def game():
    tries = 3
    target  =  random.randint(1,10)
    print("You have ",tries," tries. Enter Number:", end =" ")
    number = int(input())
    win = False
    while win != True and int(tries)>1:
        # print("whiling")
        if(target == number):
            win = True
        elif(target > number):
            tries = tries - 1
            print("Wrong! You have ",tries," tries remaining. guess bigger:", end =" ")
            number = int(input())
        elif(target < number):
            tries =  tries - 1
            print("Wrong! You have ",tries, " tries remaining. guess smaller:", end =" ")
            number = int(input())

     if(target == number):
            win = True
    if(win):
        print("You Win, the number was ",target, "!")
    else:
        print("All tries exhaused! The number was ",target,  ", better luck next time!")

    print("Do you want to play again? (Y/N) :", end =" ")
    ch = str(input())
    if (ch == "Y" or ch == "y"):
        return True
    elif(ch == "N" or ch == "n"):
        return False

print("WELCOME TO THE GUESSING GAME. GUESS THE NUMBER RIGHT AND WIN!")
while(game()):
    #do nothing
    ttt = 1

print("Terminating! See you soon. :)")