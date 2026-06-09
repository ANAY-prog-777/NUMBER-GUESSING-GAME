import random 

print(''' WELCOME TO THE NUMBER GUESSING GAME 
      I am thinking of a number between 1 and 100. Can you guess it?
     HOPE YOU ENJOY THE GAME!''')

print('''-------------------------------------------------------------------------------------------''')
print("---------------------------------------------------------------------------------------------")


RULES = input("DO YOU WANT TO KNOW THE RULES OF THE GAME?? (YES/NO) ")
if RULES.upper() == "YES":
    print("THE RULES ARE SIMPLE , YOU HAVE TO GUESS THE NUMBER IN 7 ATTEMPTS , IF YOU GUESS THE NUMBER IN LESS THAN 7 ATTEMPTS YOU WIN , IF YOU DONT GUESS THE NUMBER IN 7 ATTEMPTS YOU LOSE , GOOD LUCK!!")


print(''' ______
        .-        -.
       /            \
      |              |
      |,  .-.  .-.  ,|
      | )(_o/  \o_)( |
      |/     /\     \|
      (_     ^^     _)
       \__|IIIIII|__/
        | \IIIIII/ |
        \          /
         `--------`''')

print("THE SKULL HERE IS THE GAME OPERATOR , HE WILL BE YOUR GUIDE THROUGHOUT THE GAME, TRY NOT TO MAKE HIM ANGRY OR HE WILL EAT YOU UP IN THE END , GOOD LUCK!!")
print("THE NUMBER IS BETWEEN 1 AND 100 , YOU HAVE 7 ATTEMPTS TO GUESS THE NUMBER , GOOD LUCK!!")

random_number= random.randint(1,100)
attempts=7

while attempts > 0:
    guess = int(input("Enter your guess xoxo[:- "))


    print("------------------------------------------------------------------------------------------------------------------")




    if guess <random_number:
        print("-->YOU ARE GOING UNDERGROUND , ARE U A MINER??")
        print("--->YOU GOTTA MOVE UP UP UP UP JUST LIKE A BALLLOON")
                          




    elif guess > random_number:
            print("-->YOU ARE GOING TO THE SPACE, ARE U A ELON??")
            print("--->YOU GOTTA MOVE DOWN DOWN DOWN DOWN JUST LIKE A ELON RESUABLE ROCKET")
           
            # IM JUST AN ELON FAN BOY




    elif guess == random_number:
                print("-->CONGRATS U LANDED AND U HAVE MY RESPECT FOR GUESSING THE NUMBER , HOPE WE WILLL MEET AGAIN")
                print("SKULL IS HAPPY FOR U , HE WANTS TO CELEBRATE WITH U BUT HE WANTS TO EAT U UP TOO , SO HE WILL JUST WATCH U DANCE IN THE CELEBRATION PARTY")
                break
    
    attempts = attempts - 1

    print(f"you have {attempts} attempts left , gottta move carefully")
    




                
    if attempts == 0:
                    print("                 YOU RAN OUT OF FUEL AND BYE BYE BYE /(IN DEADPOOL STYLE)")


                    print("SKULL IS SAD FOR U , HE WANTS TO CELEBRATE WITH U BUT HE WANTS TO EAT U UP TOO , SO HE WILL JUST WATCH U DIE IN THE CELEBRATION PARTY")


                    print("---------------------------------------------------------------------------------------------------")

















































































