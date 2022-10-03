def askNumbers():
    number1 = int(input("What your first number: "))
    number2 = int(input("What your second number: "))
    return number1, number2

def askAnswer():
    number3 = int(input("What your answer: "))
    return number3
  
def checkIfRight(number1, number2):
    solution = number1 + number2
    return solution

def outretries(number1, number2, number3, solution, memory):
    if number3 == solution:
            print("Correct Answer: ", solution)
            print("You got it Correct! ")
    while number3 != solution:
        print("You Got it wrong, Try again") 
        number3 = askAnswer()
        if number3 != solution:
            print("You ran out of tries")
            print("The Correct answer is: ", solution)
            print("Your incorrect answer was: ", number3)
            number3 = solution
            continue
        if number3 == solution:
            print("Correct Answer: ", solution)
            print("You got it Correct! ")
            
            continue
    print("Done")    

def checkerAdd():
    howMany = int(input("how many problems would you like to check: "))
    memory = [""]
    tries = 0
    op = "+"
    
    for i in range(0, howMany):
        print("What is your Problem?")
        number1, number2 = askNumbers()
        number3 = 0
        solution = checkIfRight(number1, number2)
        number3 = askAnswer()
        memory = outretries(number1, number2, number3, solution, memory)
        i += 1

checkerAdd()
"""
Version 1

In this version I added all the funtions nessary 
for the addition to logically work. i left out the storing and displaying the problems.
i also have to store the track of tries.
"""