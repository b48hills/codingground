def addition(n1, n2, numberone, numbertwo):	# The addition function
    print (numberone + " + " + numbertwo + " = ")
    print (n1+n2)
    return addition
def subtraction(n1, n2, numberone, numbertwo): # The subtraction function
    print (numberone + " - " + numbertwo + " = ")
    print (n1-n2)
    return subtraction
def multiplication(n1, n2, numberone, numbertwo): # The multiplication function
    print (numberone + " * " + numbertwo + " = ")
    print (n1*n2)
    return multiplication
def division(n1, n2, numberone, numbertwo): # The division function
    print (numberone + " / " + numbertwo + " = ")
    print (n1/n2)
    return division
def all(n1, n2, numberone, numbertwo): # Run all of the functions
    addition(n1, n2, numberone, numbertwo)
    subtraction(n1, n2, numberone, numbertwo)
    multiplication(n1, n2, numberone, numbertwo)
    division(n1, n2, numberone, numbertwo)
    return all
def finish(): # Decision function to end or restart
    choice = input ("Do you want another? >").lower()
    if (choice == "yes"):
        start()
    elif (choice == "y"):
        start()
    elif (choice == "no"):
        end()
    elif (choice == "n"):
        end()
    return finish
def end(): # Function to end the program based on user choice
    print ("Thank you for playing!")
    return end
def start(): # The first function the program, directs the program based on user choice.
    print ("Adition, Subtraction, Multipliccation, Division?")
    decision = input("Please select an action. >").lower()
    numberone = input("First Number? >")
    numbertwo = input("Second number? >")
    n1 = int(numberone)
    n2 = int(numbertwo)
    if (decision == "addition"):
        addition(n1, n2, numberone, numbertwo)
    elif (decision == "a"):
        addition(n1, n2, numberone, numbertwo)
    elif (decision == "subtraction"):
        subtraction(n1, n2, numberone, numbertwo)
    elif (decision == "s"):
        subtraction(n1, n2, numberone, numbertwo)
    elif (decision == "multiplication"):
        multiplication(n1, n2, numberone, numbertwo)
    elif (decision == "m"):
        multiplication(n1, n2, numberone, numbertwo)
    elif (decision == "division"):
        division(n1, n2, numberone, numbertwo)
    elif (decision == "d"):
        division(n1, n2, numberone, numbertwo)
    elif (decision == "all"):
        all(n1, n2, numberone, numbertwo)
    finish()
    return start

start() # Command to call the first function in the program.
