import time
import math
def compte_a_rebours(n):
    if n<=0:
        print('Finish')
    else:
        
        
        time.sleep(1)
        print(n)
        compte_a_rebours(n-1)
        
a =float (input('side a: '))
b =float (input('side b: '))

c =math.sqrt(a**2 + b**2)
print('side c:', c)

t= time.time()

secs=int(t)
sec=secs % 60
mins=secs // 60

print(t)
print(secs, sec, mins)

