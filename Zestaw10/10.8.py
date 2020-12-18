from random_queue import RandomQueue
import random

randomQueue = RandomQueue()

for i in range(10):
    randomQueue.put(random.randint(0, 10))
print(randomQueue)

while not randomQueue.is_empty():
    print(randomQueue.get())
