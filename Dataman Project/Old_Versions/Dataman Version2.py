def askNumbers():
    number1 = int(input("What your first number: "))
    number2 = int(input("What your second number: "))
    return number1, number2

def askAnswer():
    number3 = int(input("What your answer: "))
    return number3
  
def checkIfRightAdd(number1, number2):
    solution = number1 + number2
    return solution

def outretries(number1, number2, number3, solution, tries):
    
    if number3 == solution:
            print("Correct Answer: ", solution)
            print("You got it Correct! ")
            tries += 1
            return tries

    while number3 != solution:
        print("You Got it wrong, Try again") 
        tries += 1
        number3 = askAnswer()
        if number3 != solution:
            print("You ran out of tries")
            print("The Correct answer is: ", solution)
            print("Your incorrect answer was: ", number3)
            number3 = solution
            tires += 1
            return tries
        if number3 == solution:
            print("Correct Answer: ", solution)
            print("You got it Correct! ")
            tries += 1
            return tries
    print("Done")    

def checkerAdd():
    howMany = int(input("how many problems would you like to check: "))
    memory = [""]
    tries = 0
    op = "+"
    howMany += 1
    for i in range(1, howMany):
        print("What is your Problem?")
        number1, number2 = askNumbers()
        number3 = 0
        solution = checkIfRightAdd(number1, number2)
        number3 = askAnswer()
        tries = outretries(number1, number2, number3, solution, tries)
        store = str(number1) + "/" + str(number2) + "/" + str(solution)
        print(store)
        memory.append(store)
    
    print("Tries: ", tries)       

checkerAdd()
"""
Version 2

In this version i added the memory feature and perfected 
the checkeradd and outretries function.
store_and_extract.py is how i stored the objects.
"""