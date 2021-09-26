#### PART 1: INTRO TO PYTHON ####

#### Hello World







#### Data types
## strings - plain text. Numbers work more like letters. "Contenation" is just putting them together. 
print("4" + "3")

## integers - Numbers without decimal values
print(4 + 3)

## floats - ___Number with decimal values___
print(4.0 + 3.0)

## a mix of types ##
print("4" + 3)

#### QUICK NOTES:
## Adding two strings is called ___________



#### Data type conversion 
## This first example converts the _integer_________ 3 into  a string__ _______ and then concatenates.
print("4" + str(3))

## This second example converts the _string _________ "4" into __ _______ and then adds.
#print(int("4") + 3)





#### PART 2: USER INPUT ####
## The input function automatically captures input as a __string_______
name = input("what is your name?")
print("Hello", name)

## To capture other types of data, be sure to convert it as a type 
user_age = int(input("what is your age?"))
print("Wow, I'm", user_age, "too!")



##### EXAMPLE 1:
name = input("what is your name?")
if name == "Jeff":
   print("Welcome to the program!")
   print("The secret message is: Janelle Monae is v. v. cool.")
 print("Program over. Shutting down.")
### Questions before running:
# How many lines will print if I tell the computer my name is "Jeff"?
# How many lines will print if I tell the computer my name is "jeff"?


### EXAMPLE 2
name = input("what is your name?")
if name == "Jeff":
   print("Welcome to the program!")
   print("The secret message is: Janelle Monae is v. v. cool.")
else:
   print("Unauthorized User. Only Jeff can use this computer.")
 print("Program over. Shutting down.")
### Questions before running:
# How is this version different from the last one?
# Why is this version of the program better than the last one? 


### EXAMPLE 3
name = input("what is your name?")
if name == "Jeff":
  user_age = int(input("What is your age? "))
  if user_age > 30:
    print("You look about", user_age-30, "years older than Jeff. Intruder detected!")
  elif user_age < 30:
    print("You are too young to be Jeff!")
  else:
   print("Welcome to the program!")
   print("The secret message is: Janelle Monae is v. v. cool.")
else:
  print("Unauthorized User. Only Jeff can use this computer.")
  input("Press return to continue")
print("Program over. Shutting down.")
## Questions before running:
##What will happen if I tell it my name is Jeff and I'm 40 years old? (right name, wrong age)
##What will happen if I tell it my name is Alyssa and I'm 30 years old? (right age, wrong name)




##### QUICK NOTES
## IF and ELSE lines end with colons and are called conditionals
## Indentation determines what belongs to a conditional and where it ends.
## Use inputs (that aren't saved to variables) to add in pauses for the user. 