 
import random 

print("로또추첨~")

for i in range(5) :
    lotto = random.sample(range(1, 46), 6)
    print(lotto)


