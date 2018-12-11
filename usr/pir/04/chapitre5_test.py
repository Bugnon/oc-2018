import time


nom=input('Quel est votre nom\n')

def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)
        

