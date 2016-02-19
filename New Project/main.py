mynumber = 7
def start():
    numbone = input("What number am I thinking of? 1 - 10. > ")
    n1 = int(numbone)
    guessing(n1)
    return start
    
def guessing(n1):
    if (n1 >= 11):
        print ("Your quess is out of range, try again 1 - 10.")
        start()
    elif (n1 == mynumber):
        print ("That's it! Yay!")
    elif (n1 < mynumber):
        print ("Nope, too low.")
        print ("Try Again.")
        start()
    elif (n1 > mynumber):
        print ("Nope, too high.")
        print ("Try Again.")
        start()
    return guessing
start()
