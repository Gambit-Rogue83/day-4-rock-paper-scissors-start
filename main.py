rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
game_images = [rock, paper, scissors]

user_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))
if user_choice >= 3 or user_choice < 0:
  print('You provided an invalid option, you lose!')
else:
  print(game_images[user_choice])

  opp_choice = random.randint(0, 2)
  print('Computer chose: ')
  print(game_images[opp_choice])
  
  if user_choice == 2 and opp_choice == 0:
    print('You lose')
  elif user_choice == 0 and opp_choice == 2:
    print('You win!')
  elif user_choice > opp_choice:
    print('You win!')
  elif user_choice < opp_choice:
    print('You lose')
  else:
    print('You tied')
  


