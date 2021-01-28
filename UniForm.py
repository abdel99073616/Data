from numpy import random

x = random.uniform(size=(2, 3))

s = random.uniform(60,120,size=(1000,19))


print ( [list( map(int,i) ) for i in s] )

