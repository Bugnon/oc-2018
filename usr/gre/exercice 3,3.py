## Exercice 3.3

def print_square(n):
    line1 = ("+ " + "- "*n)*2 + "+"
    line2 = ("| " + "  "*n)*2 + "|"
    
    print(line1)
    print((line2+ "\n")*n, end="")
    print(line1)
    print((line2+ "\n")*n, end="")
    print(line1)