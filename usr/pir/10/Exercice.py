t=[1, 2, 3, 4, 5]
v=[4, 3, 2, 1]

def cumulative(l):
    cumulative_sum=0
    new_list=[]
    for i in l:
        cumulative_sum += i
        
    new_list.append(cumulative_sum)
    return new_list

def middle(x):
    return x[1:-1]

def ordre(x):
    x.sort()
    return x

def is_anagram(text1, text2):
    return sorted(text1) == sorted(text2)

#print(is_anagram('abba', 'baba'))
#print(is_anagram('lol', 'kol'))
#print(is_anagram('a', 'b'))
#print(is_anagram('', 'a'))

    
def A(x):
    q=x+1
    return q

