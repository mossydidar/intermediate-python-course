import random

def main():
  #print('You rolled a die')
  #roll = 5
  #print(f'You rolled a {roll}')
  #roll = random.randint(1, 6)
  #print(f'You rolled a {roll}')
  #4

  dice_rolls = 2
  dice_sum = 0
  for i in range(0, dice_rolls):
    roll = random.randint(1, 6)
    dice_sum += roll
    print(f'You rolled a {roll}')
  print(f'You have rolled a total of {dice_sum}')

if __name__== "__main__":
    main()