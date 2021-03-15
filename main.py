import random
import time
r = str(random.randint(0,1000))

with open('a_'+r, 'w') as f:
    f.write('hihi')
time.sleep(200)