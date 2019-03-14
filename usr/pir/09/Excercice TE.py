fin=open ('scrabble.txt')
#ligne = fin.readline()
#mot = ligne.strip
#for ligne in fin:
#   mot=ligne.strip()
#    print(mot)

def n_a_aucun_E(mot):
    for E in mot:
        if E == 'E':
            return False
        return True 
        