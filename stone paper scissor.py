import random
n=int(input("enter no of time playing:"))
user_points=0
comp_points=0
i=0
while i<n :
    print("enter your choice \n 1-STONE \n 2-PAPER \n 3-SCISSORS")
    choice= int(input("ENTER YOUR CHOICE:"))
    if choice >3 :
        choice=int(input("ENTER VALID CHOICE:"))
    elif choice==1:
        choice_name="STONe"
    elif choice==2:
        choice_name="PAPEr"
    else:
        choice_name="SCISSORs"
    print("USER INPUT:",choice_name)
    print("\n")
    print("It's computer's turn")
    comp_choice=random.randint(1,3)
    while comp_choice==choice:
        comp_choice=random.randint(1,3)
    if comp_choice==1:
        comp_choice_name="sTONE"
    elif comp_choice==2:
        comp_choice_name="pAPER"
    else:
        comp_choice_name="sCISSORS"
    print("COMPUTER INPUT:", comp_choice_name)
    # if comp_choice==choice:
    #     print("draw")
    #     result='draw'
    if (choice == 1 and comp_choice == 2):
        print('paper wins =>', end="")
        result = 'pAPER'
    elif (choice == 2 and comp_choice == 1):
        print('paper wins =>', end="")
        result = 'PAPEr'

    if (choice == 1 and comp_choice == 3):
        print('Rock wins =>\n', end="")
        result = 'STONe'
    elif (choice == 3 and comp_choice == 1):
        print('Rock wins =>\n', end="")
        result = 'sTONE'

    if (choice == 2 and comp_choice == 3):
        print('Scissors wins =>', end="")
        result = 'sCISSORS'
    elif (choice == 3 and comp_choice == 2):
        print('Scissors wins =>', end="")
        result = 'SCISSORs'
    if result=='draw':
        print("it's a tie")
    elif result==choice:
        print("user wins")
        user_points+=10
    else:
        print("computer wins")
        comp_points+=10
    print("-------------------------")
    i+=1
if user_points > comp_points:
    print("USER WINS THE MATCH")
elif comp_points>user_points:
    print("COMPUTER WINS THE MATCH")
else:
    print("MATCH DRAW")

