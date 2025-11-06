# Getting User Input and Displaying Types
name = input("Enter your name: ")

# Getting User Input for Number of Kits Owned
kits_owned = int(input("Enter the number of kits you own: "))

# Displaying a Message with User's Name and Kits Owned
print(f"Hi {name}! You own {kits_owned} kits.")

# Displaying Data Types of Variables
print(type(name), type(kits_owned))

#-------------------------------------------------
# Day 2: Branching logic with if-else statements
#-------------------------------------------------

# Asks the user for the number of kits they own
if kits_owned == 0:
    print("You don't own any kits. Time to start your collection!")
elif kits_owned < 5:
    print("You have a small collection of kits!")
elif kits_owned <= 15:
    print("You have a decent collection of kits!")
else:
    print("Wow! You have a massive backlog of kits!")

# Creates a dictionary of valid grades
grades = {"HG", "RG", "MG", "MGEX", "PG", "PGU"}

# Asks the user for their favorite grade until a valid input is given
while True:
    grade = input("What is your favorite grade to build? (HG, RG, MG, MGEX, PG, PGU): ").upper().strip() # .upper converts to uppercase and .strip removes any spaces before or after text
    if grade in grades:
        break           # Valid input, exit the loop
    print("Invalid grade. Please choose from the given choices.")


# Responds based on the user's favorite grade and describes it
if grade == "HG":
    print("High Grades are affordable and a good way to learn for beginners.")
elif grade == "RG":
    print("Real Grades are the same size as High Grades but offer as much detail as Master Grades.")
elif grade == "MG":
    print("Master Grades offer an amazing ratio of size and detail")
elif grade == "MGEX":
    print("There are only a few Master Grade Extreme kits, and they offer as much detail as Perfect Grades in a smaller package.")
elif grade == ["PG"]:
    print("Perfect Grades are the largest of the models and offer the most detail, but they are expensive and take up a lot of space.")
elif grade == "PGU":
    print("Perfect Grade Unleashed kits are the ultimate in detail and complexity, they feature advanced gimmicks and even more detail.")
else:
    #The branch will not run because there was not a valid input
    print("Error: Invalid grade encountered.")
# Demonstrates string repetition vs numerical multiplication

