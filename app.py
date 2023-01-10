# Higher lower game
# import pprint
import random
from data import data

score = 0
end = False

pick1 = random.choice(data)
pick2 = random.choice(data)
celeb_A = pick1

while pick2 == pick1:
  pick2 = random.choice(data)

celeb_B = pick2

while end == False:
  print(f"A: {celeb_A['name']}, {celeb_A['description']} from {celeb_A['country']}")
  print("                     VS")
  print(f"B: {celeb_B['name']}, {celeb_B['description']} from {celeb_B['country']}")
  user_pick = input("Who has more followers?: ")


