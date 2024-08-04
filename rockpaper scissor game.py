import random
options = ("rock","paper" ,"scissors") 
running=True
while running:
    player = None
    computer = random.choice(options)
    while player not in options:
        player=input("enter your choice").lower()
    print(f"player : {player}")
    print(f"computer : {computer}")
    if player==computer:
        print("its a tie")
    elif player=="rock" and computer==" scissors":
        print("you wins")
    elif player=="scissors" and computer=="paper":
        print("you wins")
    elif player=="paper" and computer=="scissors":
        print("you wins")
    else:
        print("you lose")
        
    if not input("play again (y/n)").lower()=="y":
        running= False
print("Thanks for playing")            
