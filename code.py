import turtle
import math

kiki = turtle.Turtle(shape = "turtle")
kiki.speed(0)

turtle.degrees()

length = float(input("How big do you want the shapes to be? "))
while True:
    try:
        max_blocks = int(input("How many rows do you want? (Must be a whole number) "))
    except ValueError:
        print("That's not an WHOLE number!")
        continue
    else:
        break
while True:
    try:
        stacks = int(input("How many columns do you want? (Must be a whole number) "))
    except ValueError:
        print("That's not an WHOLE number!")
        continue
    else:
        break

always_row = stacks
take_it_back = always_row * length * 2
hexy_height = math.sqrt(round(3,6)) * length
done = stacks * max_blocks
pensize = (0.05 * length)

turtle.TurtleScreen
turtle.setup(width=900, height=800, startx=None, starty=None) 
kiki.penup()
kiki.setx(-700)
kiki.sety(300)
kiki.pendown()

pink = '#ff61ad'
mint = '#bdffeb'
lilac = '#d7bdff'
sunshine = '#fff8a6'

end_me = 0
blocks = 0

def Star(pensize, num_sides, length, lines, color):
    kiki.pensize(pensize)
    kiki.pencolor(lines)
    kiki.fillcolor(color)
    kiki.begin_fill()
    for sides in range(0,num_sides):
        degrees = 360 / num_sides
        kiki.forward(length)
        kiki.left(degrees)
    kiki.end_fill()

def Move1(take_it_up):
    kiki.penup()
    kiki.forward(take_it_up)
    kiki.pendown()

def Move2(to_the_side):
    kiki.right(120)
    kiki.backward(to_the_side)
    kiki.left(120)

def Move3(to_the_front):
    kiki.penup()
    kiki.right(90)
    kiki.forward(to_the_front)
    kiki.left(90)
    kiki.pendown()

def Move4(take_it_back, to_the_front):
    kiki.penup()
    kiki.back(take_it_back)
    kiki.right(90)
    kiki.forward(to_the_front)
    kiki.left(90)
    kiki.pendown()

while blocks < always_row:
        for reps in range(0, stacks):
            Star(pensize,6,length,lilac,pink)
            Move1(length)
            Star(pensize,3,length,sunshine,mint)
            Move2(length * 2)
            Star(pensize,3,-length,sunshine,mint)
            Move3(hexy_height)
            blocks += 1
            end_me += 1
            if end_me == done:
                break
            elif blocks == always_row:      
                Move4(take_it_back, hexy_height)
                blocks = 0

turtle.mainloop()
