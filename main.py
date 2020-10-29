# ітерації

import itertools
import time

from numpy import random

start_time = time.time()

elements = random.randint(1000, size=(int(input("Кількість елементів масиву : "))))

# for i in range(0, int(size)):
#     x = input("Елемент " + str(i) + " : ")
#     elements.append(x)

perm_iterator = itertools.permutations(elements)

for item in perm_iterator:
    print(item)

print("--- %s секунд ---" % (time.time() - start_time))
