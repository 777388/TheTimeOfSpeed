import time as t 
import math
Flux = lambda: Flux * (Speed **2) * (Time ** 3)
vroom = 0
for c in str(Flux):
    vroom += t.time() % ord(c)

print(math.sin(vroom))