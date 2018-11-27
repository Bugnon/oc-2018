# File name: pythagore.py
# Author: MichARom
# Date: 27.11.2018


import math
for i in range(1000):
    print('Théorème de Pythagore n°', i+1,'\n')
    a = float(input('Side a: '))
    b = float(input('Side b: '))
    
    c=math.sqrt(a**2+b**2)
    print('Side c = ',c, '\n\n\n')
