
import os

for x, y, z in os.walk('.'):
    for z1 in z:
        if os.path.getsize(os.path.join(x,z1)) > 5000:
            print(os.path.join(x,z1))
            print(os.path.getsize(os.path.join(x,z1)))