import turtle

print('J\'écris ce que vous voulez...\n\n')

word = input('Ecris ton mot: ')

a = turtle.Turtle()

a.speed(9999)

a.penup()

length = len(word)





def A():
    a.pendown()
    a.lt(70)
    a.fd(106)
    a.rt(140)
    a.fd(50)
    a.rt(110)
    a.fd(34)
    a.bk(34)
    a.lt(110)
    a.fd(57)
    a.lt(70)
    a.penup()
    a.fd(20)
    
def B():
    a.pendown()
    a.fd(20)
    a.circle(25, 180)
    a.fd(20)
    a.bk(20)
    a.rt(180)
    a.circle(25, 180)
    a.fd(20)
    a.lt(90)
    a.fd(100)
    a.lt(90)
    a.penup()
    a.fd(75)
    
def C():
    a.fd(60)
    a.rt(180)
    a.pendown()
    a.fd(10)
    a.circle(-50, 180)
    a.fd(10)
    a.penup()
    a.rt(90)
    a.fd(100)
    a.lt(90)
    a.fd(20)
    
def D():
    a.pendown()
    a.lt(90)
    a.fd(100)
    a.rt(90)
    a.fd(20)
    a.circle(-30, 90)
    a.fd(40)
    a.circle(-30, 90)
    a.fd(20)
    a.rt(180)
    a.penup()
    a.fd(80)
    
def E():
    a.pendown()
    for i in range(2):
        a.fd(30)
        a.bk(30)
        a.lt(90)
        a.fd(50)
        a.rt(90)
    a.fd(30)
    a.penup()
    a.rt(90)
    a.fd(100)
    a.lt(90)
    a.fd(20)
    
def F():
    a.pendown()
    for i in range(2):
        a.lt(90)
        a.fd(50)
        a.rt(90)
        a.fd(30)
        a.bk(30)
    a.penup()
    a.rt(90)
    a.fd(100)
    a.lt(90)
    a.fd(40)

def G():
    a.fd(60)
    a.lt(90)
    a.fd(40)
    a.lt(90)
    a.fd(30)
    a.pendown()
    a.lt(180)
    a.fd(30)
    a.rt(90)
    a.fd(40)
    a.rt(90)
    a.fd(10)
    a.circle(-50, 200)
    a.penup()
    a.rt(70)
    a.fd(97)
    a.lt(90)
    a.fd(20)
def H():
    a.pendown()
    a.lt(90)
    a.fd(100)
    a.bk(50)
    a.rt(90)
    a.fd(50)
    a.lt(90)
    a.fd(50)
    a.bk(100)
    a.rt(90)
    a.penup()
    a.fd(30)

def I():
    a.pendown()
    a.fd(30)
    a.bk(15)
    a.lt(90)
    a.fd(100)
    a.lt(90)
    a.fd(15)
    a.bk(30)
    a.penup()
    a.lt(90)
    a.fd(100)
    a.lt(90)
    a.fd(20)

def J():
    a.lt(90)
    a.fd(25)
    a.lt(180)
    a.pendown()
    a.circle(25, 180)
    a.fd(75)
    a.lt(90)
    a.fd(30)
    a.bk(30)
    a.lt(90)
    a.penup()
    a.fd(100)
    a.lt(90)
    a.fd(30)

def K():
    a.lt(90)
    a.pendown()
    a.fd(100)
    a.bk(55)
    a.rt(45)
    a.fd(72)
    a.bk(70)
    a.rt(90)
    a.fd(64)
    a.penup()
    a.lt(45)
    a.fd(30)

def L():
    a.pendown()
    a.lt(90)
    a.fd(100)
    a.bk(100)
    a.rt(90)
    a.fd(33)
    a.penup()
    a.fd(10)

def M():
    a.pendown()
    a.lt(90)
    a.fd(100)
    a.rt(150)
    a.fd(47)
    a.lt(120)
    a.fd(47)
    a.rt(150)
    a.fd(100)
    a.penup()
    a.lt(90)
    a.fd(30)

def N():
    a.pendown()
    a.lt(90)
    a.fd(100)
    a.rt(150)
    a.fd(115.47)
    a.lt(150)
    a.fd(100)
    a.bk(100)
    a.penup()
    a.rt(90)
    a.fd(30)

def O():
    a.lt(90)
    a.fd(25)
    a.rt(180)
    a.pendown()
    for i in range(2):
        a.circle(25, 180)
        a.fd(50)
    a.penup()
    a.fd(25)
    a.lt(90)
    a.fd(80)
    
def P():
    a.lt (90)
    a.pendown()
    a.fd(100)
    a.rt(90)
    a.fd(15)
    a.circle(-25, 180)
    a.fd(15)
    a.penup()
    a.lt(90)
    a.fd(50)
    a.lt(90)
    a.fd(60)
    
def Q():
    O()
    a.bk(20)
    a.pendown()
    a.lt(135)
    a.fd(40)
    a.bk(40)
    a.rt(135)
    a.penup()
    a.fd(20)

def R():
    P()
    a.lt(180)
    a.fd(16.2)
    a.pendown()
    a.rt(60)
    a.fd(57.73)
    a.bk(57.73)
    a.penup()
    a.rt(120)
    a.fd(20)

def S():
    a.pendown()
    a.fd(10)
    a.circle(25, 180)
    a.circle(-25, 180)
    a.fd(10)
    a.penup()
    a.rt(90)
    a.fd(100)
    a.lt(90)
    a.fd(30)

def T():
    a.fd(40)
    a.lt(90)
    a.pendown()
    a.fd(100)
    a.lt(90)
    a.fd(40)
    a.bk(80)
    a.lt(90)
    a.penup()
    a.fd(100)
    a.lt(90)
    a.fd(20)

def U():
    a.lt(90)
    a.fd(100)
    a.pendown()
    a.lt(180)
    a.fd(75)
    a.circle(25, 180)
    a.fd(75)
    a.penup()
    a.bk(100)
    a.rt(90)
    a.fd(20)

def V():
    a.lt(90)
    a.fd(100)
    a.rt(160)
    a.pendown()
    a.fd(106.42)
    a.lt(140)
    a.fd(106.42)
    a.penup()
    a.rt(160)
    a.fd(100)
    a.lt(90)
    a.fd(20)
    
def W():
    a.lt(90)
    a.fd(100)
    a.rt(165)
    a.pendown()
    a.fd(103.52)
    a.lt(150)
    a.fd(51.76)
    a.rt(150)
    a.fd(51.76)
    a.lt(150)
    a.fd(103.52)
    a.penup()
    a.rt(165)
    a.fd(100)
    a.lt(90)
    a.fd(20)

def X():
    a.lt(55)
    a.pendown()
    a.fd(122.07)
    a.bk(61.04)
    a.lt(70)
    a.fd(61.04)
    a.bk(122.07)
    a.penup()
    a.rt(125)
    a.fd(20)
    
def Y():
    a.lt(55)
    a.pendown()
    a.fd(122.07)
    a.bk(61.04)
    a.lt(70)
    a.fd(61.04)
    a.penup()
    a.bk(122.07)
    a.rt(125)
    a.fd(20)
    

def Z():
    a.pendown()
    a.fd(100)
    a.bk(100)
    a.lt(45)
    a.fd(70.71)
    a.rt(45)
    a.fd(20)
    a.bk(40)
    a.fd(20)
    a.lt(45)
    a.fd(70.71)
    a.lt(135)
    a.fd(100)
    a.bk(100)
    a.penup()
    a.lt(90)
    a.fd(100)
    a.lt(90)
    a.fd(30)
    
for c in word:
    if c == 'a':
        A()
    elif c == 'b':
        B()
    elif c == 'c':
        C()
    elif c == 'd':
        D()
    elif c == 'e':
        E()
    elif c == 'f':
        F()
    elif c == 'g':
        G()
    elif c == 'h':
        H()
    elif c == 'i':
        I()
    elif c == 'j':
        J()
    elif c == 'k':
        K()
    elif c == 'l':
        L()    
    elif c == 'm':
        M()
    elif c == 'n':
        N()
    elif c == 'o':
        O()
    elif c == 'p':
        P()
    elif c == 'q':
        Q()
    elif c == 'r':
        R()
    elif c == 's':
        S()
    elif c == 't':
        T()
    elif c == 'u':
        U()
    elif c == 'v':
        V()
    elif c == 'w':
        W()
    elif c == 'x':
        X()
    elif c == 'y':
        Y()
    elif c == 'z':
        Z()