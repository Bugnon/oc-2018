def do_twice (f):
    F()
    F()

def do_four(f):
    do_twice(f)
    do_twice(f)

def print_beam ():
    print('+----', end = '')
    
def print_post():
    print('/', end ='')
    
def print_beams():
    do_twice (print_beam)
    print('+')
    
def print_posts ():
    do_twice (print_posts)
    print_beams ('/')
    
def print_row ():
    print_beams ()
    do_four(print_posts)
    
def print_grid ():
    do_twice(print_row)
    print_beams()
    



