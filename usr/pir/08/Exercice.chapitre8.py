#Mirko Pirona
#03.12.2018
#Chapitre 8

#Exercice 1:

def x():
    '    monty    '.strip()
    
def y():
    'monty'.replace('t', 'ke')

#Exercice 2:
    
def count():
    count('banana', 'a')
    
#Exercice 3:
    
s='monty python'

def slice2():
    s[::2]
    
#Exercie 4
    
#Est-ce que la première lettre est minuscule?
#Retourne toujours true
#Est-ce que la dernière lettre est minuscule?
#Est-ce qu'il a au moin une lettre minuscule?
#Est-ce que toutes le lettres sont minuscules?
    
#Exercice 5:
    
def rotate_word(s, n):
    res= ''
    for c in s:
        m=ord(c) + n
        if m > ord('z'):
            m -= 26
        res += chr(m)
    return res

