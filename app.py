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



