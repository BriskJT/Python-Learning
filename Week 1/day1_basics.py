#------------------------------------------------
# Day 1: Variables, Data Types, and User Input
#-------------------------------------------------

#Get input for the user's name
name = input("Enter your name: ") 

#Get input how hmany kits the user owns.
kits_owned = int(input("Enter the number of kits you own: ")) 

#Print a message including the user's name and number of kits owned
print(f"Hi {name}! You own {kits_owned} kits.")

#Print the data types of the variables
print(type(name), type(kits_owned))

#kits_owned = input("How many kits do you own? ")
#print(kits_owned * 2) #Shows string repitition

#kits_owned = int(input("How many kits do you own? "))
#print(kits_owned * 2)   #Shows numerical multiplication