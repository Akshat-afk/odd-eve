import random

class batter:
    def __init__(self,runs,is_out,has_won,has_batted,in_superover):
        self.runsmade = runs
        self.isout = is_out
        self.haswon = has_won
        self.hasbatted = has_batted
        self.insuperover = in_superover

def user():
    while True:
        user_input = int(input(">>> "))
        if user_input in range(1,11):
            break
        else:
            pass
    return user_input

def comp():
    comp_input = random.randint(1,10)
    return comp_input


global player
player = batter(0,False,False,False,False)

global computer
computer = batter(0,False,False,False,False)

        

def balling():

    print("You are balling rn")
    
    while computer.isout == False and computer.haswon == False:
        ball_num = user()
        bat_num = comp()
        
        if ball_num == bat_num:
            print(f"Computer chose {bat_num}.")
            print(f"Computer is out and made {computer.runsmade} runs.")

            if computer.runsmade == player.runsmade and computer.hasbatted == True and player.hasbatted == True:
                computer.insuperover = True
                player.insuperover = True
            
            break
        else:
            computer.runsmade += bat_num
            print(f"Computer chose {bat_num}.")
            if computer.runsmade > player.runsmade and player.hasbatted == True:
                computer.haswon = True
                print(f"Computer has won by {computer.runsmade - player.runsmade} runs.")
                break
            elif computer.runsmade == player.runsmade and computer.hasbatted == True and player.hasbatted == True:
                computer.insuperover = True
                player.insuperover = True
    computer.hasbatted = True
    

def batting():

    print("You are batting rn")

    while player.isout == False:
        ball_num = comp()
        bat_num = user()
        
        if ball_num == bat_num:
            print(f"Computer chose {ball_num}.")
            print(f"You are out and made {player.runsmade} runs.")
            
            if computer.runsmade == player.runsmade and computer.hasbatted == True and player.hasbatted == True:
                computer.insuperover = True
                player.insuperover = True
            break
        else:
            player.runsmade += bat_num
            print(f"Computer chose {ball_num}.")   
            if computer.runsmade < player.runsmade and computer.hasbatted == True:
                player.haswon = True
                print(f"You have won by {player.runsmade - computer.runsmade} runs.")     
                break
            elif computer.runsmade == player.runsmade and computer.hasbatted == True and player.hasbatted == True:
                computer.insuperover = True
                player.insuperover = True
    player.hasbatted = True
    
def win():
    if player.haswon == True or computer.haswon == True:
        pass
    else:
        if player.runsmade > computer.runsmade:
            print("You have won")
        else:
            print("The computer has won")

def super_over():
    if computer.insuperover ==True and player.insuperover == True:
        print("This is a super over and you will have 6 balls to make as many runs as possible")
        player.isout = False
        computer.isout = False
        player.hasbatted = False
        computer.hasbatted = False
        player.runsmade = 0
        computer.runsmade = 0

        print("You are batting rn")
        for i in range(6):
            ball_num = comp()
            bat_num = user()

            if ball_num == bat_num:
                print(f"Computer chose {ball_num}.")
                print(f"You are out and made {player.runsmade} runs.")
                break
            else:
                player.runsmade += bat_num
                print(f"Computer chose {ball_num}.")   
                if computer.runsmade < player.runsmade and computer.hasbatted == True:
                    player.haswon = True
                    print(f"You have won by {player.runsmade - computer.runsmade} runs.")     
                    break
        
        print("You are balling rn")
        for i in range(6):
            ball_num = user()
            bat_num = comp()

            if ball_num == bat_num:
                print(f"Computer chose {bat_num}.")
                print(f"Computer is out and made {computer.runsmade} runs.")
                break
            else:
                computer.runsmade += bat_num
                print(f"Computer chose {bat_num}.")
                if computer.runsmade > player.runsmade and player.hasbatted == True:
                    computer.haswon = True
                    print(f"Computer has won by {computer.runsmade - player.runsmade} runs.")
                    break

        if computer.runsmade > player.runsmade:
            print(f"The computer has won the super over by {computer.runsmade-player.runsmade}")
        elif computer.runsmade < player.runsmade:
            print(f"The player has won the super over by {player.runsmade-computer.runsmade}")
        else:
            print("It was a tie again another super over will be played")
            super_over()
def bat():
    
    batting()
    balling()
    if computer.runsmade == player.runsmade and computer.hasbatted == True and player.hasbatted == True:
        computer.insuperover = True
        player.insuperover = True
        super_over()
    win()

def ball():

    balling()
    batting()
    if computer.runsmade == player.runsmade and computer.hasbatted == True and player.hasbatted == True:
        computer.insuperover = True
        player.insuperover = True
        super_over()

    win()

print('''Welcome to Odd Eve
RULES:
1) There is a toss first to decide who is batting and balling
2) The objective of the batter is to score as many runs as possible by choosing a number between 1 to 10
3) The objective of the baller is to choose the same number as the batter to get a wicket
4) At the end whoever has the higher score wins the game
5) Have fun!!!''')

l = [bat,ball]
random.choice(l)()

