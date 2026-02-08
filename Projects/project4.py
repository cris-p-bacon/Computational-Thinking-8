import turtle, time, random
from utils import *

# The goal of this game is to collect money and buy apples. 
# Press "m" to get money and press "a" to buy apples

# ***************************************
# Section 1 - SETUP 
# ***************************************

# Set a background using set_background()
set_background("underwater")

# ****************************************************************************
# Create at least two variables and set their starting value, ex: cookies = 0
# ****************************************************************************

money = 0
apples = 0

# OPTIONAL: use this invisible alien to say a message
message_sprite = create_sprite("alien", -200,200)
message_sprite.hideturtle()


# ***************************************
# Section 2 - CONTROLS
# ***************************************

# Define an action. ex: def my_control()

# ********************
# Define first action
# ********************
# This function gives you money in increments of 15. The "m" key invokes this function.
def get_money():
    global money
    money += 15
    print("You just got more money. Now you have {money} dollars.")

# *********************
# Define second action
# *********************
# This function buys and spawns apples if you have enough money. The "a" key invokes this function. 
def buy_apple():
    global apples;global money  
    if money >= 3:
        money -= 3
        apples += 1
        x = random.randint(-300,300)
        y = random.randint(-300,300)
        create_sprite("applecore", x, y)
        print("You paid $3 for an apple. Now you have {money} dollars and {apples} apples.")


# **************************************************************************
# Choose a key to do the action. ex: window.onkeypress(my_control, "space")
# **************************************************************************
window.onkeypress(get_money, "m")
window.onkeypress(buy_apple, "a")


# ******************************************
# Section 3 - game loop
# ******************************************
window.listen()
for i in range(100000000000000000000000000000000):
    if i % 50 == 0:
        money += 2   
    message_sprite.clear()
    message_sprite.write(f"You have this much {money} money.\nYou have this many {apples} apples.",font=("Arial",20,"normal"))

    time.sleep(0.01)
    window.update()