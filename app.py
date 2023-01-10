# Higher lower game
# import pprint
import random
from data import data

def update(win_celeb, celeb_to_change):
  celeb_to_change = random.choice(data)

  while celeb_to_change == win_celeb:
    celeb_to_change = random.choice(data)
  
  return celeb_to_change


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
  user_pick = input("Who has more followers?A or B: ").lower()

  if user_pick == "a" and celeb_A['follower_count'] > celeb_B['follower_count']:
    celeb_B = update(celeb_A, celeb_B)
    score += 1
    print(f"Your score is {score}")
  elif user_pick == "b" and celeb_B['follower_count'] > celeb_A['follower_count']:
    celeb_A = celeb_B
    celeb_B = update(celeb_A, celeb_B)
    score += 1
    print(f"Your score is {score}")
  else:
    end = True

print(f"Your final score is {score}")
