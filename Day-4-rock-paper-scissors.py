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
import random 
you_chose = int(input())
game_list = [rock, paper, scissors ]

my_value = you_chose
computer_value  = random.randint(0,2)

print(game_list[my_value])
print(game_list[computer_value])

if my_value >= 3 or my_value < 0: 
  print("You typed an invalid number, you lose!") 
elif my_value == 0 and computer_value == 2:
  print("You win!")
elif computer_value == 0 and my_value == 2:
  print("You lose")
elif computer_value > my_value:
  print("You lose")
elif my_value > computer_value:
  print("You win!")
elif computer_value == my_value:
  print("It's a draw") 
