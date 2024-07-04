import datetime
from datetime import date
import random

conun_list = ["EXPLICATE" , "EXTORTION" , "FABRICATE" , "EXTROVERT" , " FALLOWING" , "alcoholic" , "abandoned" , "abilities" , "activated" , "adaptable" , "addicting" ,
    "amusement" ,"analytics" , "analyzing" , "enquiring" , "hijacking" , "squeezing" , "sabotaged" , "sacrifice" , "authentic" , "sarcastic" ,"satisfied" , "attacking" ,
    "defensive" ,"downright" , "perplexed" , "beautiful" , "agonizing" , "wrenching" , "formation" , "objective" , "spherical" , "empirical" , "important" , "situation" ,
    "adulthood" ,"aftermath" ,"agreeably" , "alcoholic" , "alertness" , "alternate" , "amazement" , "amazingly" , "ambitious" , "ambitions" , "amphibian" , "amusingly" ,
    "craftable" , "yesterday"
  ]

consonants = [  "B", "C", "D", "F", "G", "H", "J", "K", "L",
                "M", "N", "P", "Q", "R", "S", "T", "V", "W",
                "X", "Y", "Z", "B", "C", "D", "F", "G", "H",
                "K", "L", "M", "N", "P", "R", "S", "T", "V", "W"
            ]
vowels = ["A", "E", "I", "O", "U", "A", "E", "O", "E", "O"]

large_nums = [25, 50, 75, 100]
small_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def do_maths(a, b):
  actions_list = ["add", "sub", "mul", "div"]
  action = random.choice(actions_list)
  
  if action == "add":
      return a + b
  elif action == "sub":
      if a > b:
          return int( a - b )
      elif b > a:
          return int( b-a )
  elif action == "mul":
      return int(a * b)
  elif action == "div":
      if (a > b) and (a % b == 0):
          return int( a / b )
      elif (b > a) and ( b % a == 0 ):
          return int( b / a )
      else:
          return int(a + b)
  else:
      print('Error - This should never happen')



def generate_game():

 #generate letters for the word game
  my_letters = ''
  for cons in range(6):
      my_letters += random.choice(consonants)
  for vows in range(3):
      my_letters += random.choice(vowels)

  #choose numbers for the numbers game and generate a target
  my_nums = []

  lrg = random.choice(large_nums)
  my_nums.append(lrg)
  for sml in range(5):
      sml = random.choice(small_nums)
      my_nums.append(sml)
  main_nums = my_nums[:]
                
  i = 0
  while i < 5:
      index_a = my_nums.index(random.choice(my_nums))
      num_a = int( my_nums.pop(index_a) )
      index_b = my_nums.index(random.choice(my_nums))
      num_b = int( my_nums.pop(index_b) )
      target = do_maths(num_a , num_b)
      my_nums.append(target)

      if i == 4:
          if (target < 101) or (target > 999 ):
              my_nums = main_nums[:]
              i = 0
          else:
              i += 1
      else:
          i += 1
      my_numbers = str(main_nums)
      my_numbers = my_numbers.replace('[','')
      my_numbers = my_numbers.replace(']','')

  #get conundrum    
  conundrum = random.choice(conun_list)

  return (my_letters, my_numbers, target, conundrum)

