import random

print(random.randrange(1,12)) #returns randint from range
print(random.randint(10,200)) #alis to randrange

groceries = ['milk','bread','egg','butter']
print(random.choice(groceries)) #choose random from sequence
random.shuffle(groceries) #shuffle order
print(groceries) 