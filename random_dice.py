import turtle
import math
import random
import time

#FUNCTIONS
try:                                                            #READ LAST COMMENT
    import keyboard
    manual=False
    print("Manual=False")
except ModuleNotFoundError:
    manual=True
    step("Error while loading 'keyboard' module")
    print("Manual=True")

def step(s):
    global i
    i+=1
    print(f"{i}:: ",s.capitalize())

def bound(x,size,chaos=False,diam=15):
    x.pu()
    x.goto((size/2)-diam/2,-size/2)
    x.pd()
    x.color("black","white")
    x.begin_fill()                                              #fill dice with white color
    for i in range(4):
        x.circle(diam/2,90)
        x.fd(size-diam)
    x.end_fill()
    x.pu()
    t.home()
    x.pd()
    if chaos==False:                                            #In chaos won't print anything
        step("Dice drawed")

def face(x, num, size):                                         #draw instruction for number
    if num==1:
        x.dot(5)
    if num==2:
        for i in range(2):
            x.seth(45+i*180)
            t.pu()
            x.fd((size/4)*math.sqrt(2)*(i+1))
            t.pd()
            x.dot(5)
    if num==3:
        face(x,1,50)                                            #recursive function
        face(x,2,50)
    if num==4:
        x.lt(45)
        x.pu()
        x.fd((size/4)*math.sqrt(2))
        x.lt(45)
        for i in range(4):
            x.lt(90)
            x.fd(size/2)
            x.dot(5)
    if num==5:
        face(x,1,50)
        face(x,4,50)
    if num==6:
        x.lt(45)
        x.pu()
        x.fd((size/4)*math.sqrt(2))
        x.seth(270)
        for j in range(3):
            if j%2==0:
                for i in range(3):
                    x.dot(5)
                    if i!=2:
                        x.fd(size/4)
            else: x.fd(size/2)
            x.rt(90)

def chaos(drw, rep):                                            #generate random number
    for i in range(rep):                                        #like main loop, but repeated
        m=random.randint(1,6)
        drw.pu()
        drw.home()
        drw.pd()
        bound(drw,50,chaos=True)
        face(drw,m,50)
        turtle.update()
        time.sleep(.05)
        t.reset()

def writer(x,size,msg):                                         #print number on canvas
    x.pu()
    x.home()
    x.seth(270)
    x.fd(size*3)
    x.pd()
    global clr
    x.color(clr[random.randint(0,len(clr)-1)])
    x.write(msg,align="center",font=("Arial",25,"italic"))

#variables
i=0
size=50
clr=["red","cyan","blue","yellow","aqua"]
#basic
t=turtle.Turtle()
turtle.tracer(False)
turtle.title("Random dice generator")
t.speed(0)
#graphic
window=turtle.Screen()
window.screensize(400,400)
window.bgcolor("green")

#MAIN LOOP
while 1:
    n=random.randint(1,6)
    chaos(t,size)                                               #Random cycle
    t.pu()
    t.home()
    t.pd()
    bound(t,size)                                               #Dice drawer
    face(t,n,size)                                              #Dots drawer
    step("Displayed number "+str(n))
    writer(t,size,"Numero "+str(n))
    if manual==True:                                            #Type if 'keyboard' isn't installed
        query=input("Rerun(S/n)?\t")
        if query.lower()!="s":
            quit()
            step("Quit")
        step("Rerun")
    else:
        print("Rerun(S/n)?")                                    #Hit key if 'keyboard' is installed
        while True:
            if keyboard.is_pressed("s"):
                break
            elif keyboard.is_pressed("n"):
                quit()
    t.reset()                                                   #RESTART