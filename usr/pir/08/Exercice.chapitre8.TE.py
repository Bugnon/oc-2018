#index=-1
#fruit = 'banana'
#while index >= -(len(fruit)):
#    lettre=fruit[index]
#    print(lettre)
#    index=index -1

def trouver(mot, lettre):
    index=0
    while index < len(mot):
        if mot [index]==lettre:
            return index
        index = index+1
    return -1
