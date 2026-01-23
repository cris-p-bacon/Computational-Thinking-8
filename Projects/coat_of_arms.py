# Section 1 - Your code
from utils import *
set_background("winter")

s1 = create_sprite("cat", 100, 100)
s2 = create_sprite("677777", -100, 100)
s3 = create_sprite("pineapple", -100, -150)
s4 = create_sprite("soccerball", 150, -150)

message1 = create_sprite("alien",-200,200)
message1.color("red")
message1.write("Eric Cisyk",font = ("Arial", 40, "normal"))
message1.hideturtle()

message2 = create_sprite("alien",-200,-250)
message2.color("black")
message2.write("67 Mangoes",font = ("Arial", 40, "normal"))
message2.hideturtle()


######################################################################


# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()