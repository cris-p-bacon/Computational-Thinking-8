print("Welcome to the Personality Quiz!")
print("Select A, B, or C for each question, depending on your preferences.\n")

# Declare variables
extrovert_points = 0
introvert_points = 0
omnivert_points = 0

# Question 1
answer1 = input("Do you prefer A going to parties frequently, B rarely going to parties, or C it depends.\n")
if answer1 == "A":
    extrovert_points += 1
elif answer1 == "B":
    introvert_points += 1
elif answer1 == "C":
    omnivert_points += 1
print("------------------------------------------------------------------------------------------------------------------------------------------------------- ")

# Question 2
answer2 = input("Do you prefer A hanging out with a lot of different people, B hanging out with a core group of people, or C both.\n")
if answer2 == "A":
    extrovert_points += 1
elif answer2 == "B":
    introvert_points += 1
elif answer2 == "C":
    omnivert_points += 1
print("------------------------------------------------------------------------------------------------------------------------------------------------------- ")

# Question 3
answer3 = input("Do you A feel energized after large social gathering, B Feel drained after hanging out with a lot of people, or C both.\n")
if answer3 == "A":
    extrovert_points += 1
elif answer3 == "B":
    introvert_points += 1
elif answer3 == "C":
    omnivert_points += 1
print("------------------------------------------------------------------------------------------------------------------------------------------------------- ")

# Question 4
answer4 = input("Do you A like to work on projects with a group, B work alone, or C it depends?\n")
if answer4 == "A" or answer4 == "C":
    extrovert_points += 1
    omnivert_points += 1
elif answer4 == "B":
    introvert_points += 1
print("------------------------------------------------------------------------------------------------------------------------------------------------------- ")
answer5 = input("Do you A enjoy small talk, B find it tiresome, or C you are indifferent.\n")

# Question 5
if answer5 == "A":
    extrovert_points += 1
elif answer4 == "B":   
    introvert_points += 1
elif answer5 == "C":
    omnivert_points += 1
print("------------------------------------------------------------------------------------------------------------------------------------------------------- ")

# Print the score
print (f"Your score is {extrovert_points} extrovert, {introvert_points} introvert, and {omnivert_points} omnivert.")

# End: determine result
if extrovert_points >= introvert_points and extrovert_points >= omnivert_points:
    print("You are an Extrovert!!")
elif introvert_points >= omnivert_points and introvert_points >= extrovert_points:
    print("You are an Introvert!!")
elif omnivert_points >= extrovert_points and omnivert_points >= introvert_points:
    print("You are an Omnivert!!")