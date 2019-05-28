#Auteurs: Fabian Roulin, Mirko Pirona, Michael Greub
#Date: 23.05.2019 
import unicodedata
from time import sleep
import codecs
file1 = input('Entrer le chemin exacte du fichier source:')
file2 = input('Entrer le chemin exacte du fichier de sortie:')
fo = codecs.open(file1, 'r', 'utf-8')
done = codecs.open(file2, 'w+', 'utf-8')
string = fo.readlines()
for i in string:
    #ligne tiree d'internet
    A = ''.join((c for c in unicodedata.normalize('NFKD', i) if unicodedata.category(c) != 'Mn'))
    A = A.replace('-', '')
    A = A.lower()
    A = A.replace(' ', '\r\n')
    done.write(i)
print('Done.')
