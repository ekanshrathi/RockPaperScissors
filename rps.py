import random

rock = '''
    -------
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)      
'''
paper = '''
    ________
---'    ____)______
            _______)
            ________)
            ______)
---.___________)    
'''
scissors = '''
    _________
---,    _____)_____
            _______)
         ____________)
         (_____)
---.____(____)   
'''

game_images = [rock, paper, scissors]
user_choice = int(input('Enter your choice: Type 0 for Rock /n Type 1 for Paper /n Type 2 for Scissors'))
if user_choice < 0 or user_choice >= 3:
    print("INVALID INPUT!")
else:
    print(game_images[user_choice])
    computer_choice = random.randint(0,2)
    print("Computer chose:")
    print(game_images[computer_choice])

    if computer_choice == user_choice:
        print("Its a DRAW")
    elif computer_choice > user_choice:
        print("YOU LOSE")
    elif user_choice > computer_choice:
        print("YOU WIN")
    elif computer_choice == 0 and user_choice == 2:
        print("YOU LOSE")
    elif user_choice == 0 and computer_choice == 2:
        print("YOU WIN")
