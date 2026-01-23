import turtle, time, random
from utils import *

# Section 1 - Variables
# TODO - add starting values for all the variables
x1 =-300
y1 =-100    
x2 =-300
y2 =0
x3 =-300
y3 =50
x4 =-300
y4 =100


# Section 2 - Setup
# # TODO - use your own background, and set your four turtles to images of your choice
set_background("castle")
t1 = create_sprite("cat2",x1,y1)
t2 = create_sprite("basketball",x2,y2)
t3 = create_sprite("soccerball",x3,y3)
t4 = create_sprite("pineapple",x4,y4)


# Section 3 - Racing
# TODO - set how much each variable changes by and increase the number of repeats to at least 30
# TODO - explain here which sprites are faster or slower
for i in range(40):
    x1 += 10 # second fastest
    x2 += 5 # slowest
    x3 += 7 # second slowest
    x4 += 15 # fastest
# x4 is the fastest turtle so it will win
    t1.goto(x1, y1)
    t2.goto(x2, y2)
    t3.goto(x3, y3)
    t4.goto(x4, y4)

    window.update()
    time.sleep(0.1)


# Section 4 - Winner
# TODO - complete the elif for player 2 winning
# TODO - write another elif for player 3 and player 4
if x1 >= x2 and x1 >= x3 and x1 >= x4:
    print("Cat 1 wins!")
elif x2 >= x1 and x2 >= x3 and x2 >= x4:
    print("Basketball wins!")
elif x3 >= x1 and x3 >= x2 and x3 >= x4:
    print("Soccerball wins")
elif x4 >= x1 and x4 >= x2 and x4 >= x3:
    print("Pineapple wins!")

turtle.exitonclick()