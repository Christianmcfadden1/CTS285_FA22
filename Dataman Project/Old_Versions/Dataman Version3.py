"""
Version 3

In this version i need the input of the equations and answer to be spliced.
and store the equation and answer in the memory. program must get the 
opperation from the equation separated by " " 
"""

def askProblem():
    """
    *We dont need this when slicing a string up*
    *Also changing name to askProblem()*
    number1 = int(input("What your first number: "))
    number2 = int(input("What your second number: "))
    return number1, number2

    """
    guess = input("Please enter your equation (Separate it by spaces): ")
    return guess
    
"""
*We dont need this when slicing a string up*
*Actually we do incase they get it wrong.*
"""
def askAnswer():
    number3 = int(input("What your answer: "))
    return number3

"""
def checkIfRightAdd(number1, number2):
*Change the function name to getSolutionAdd(number1, number2)*
"""
def getSolutionAdd(number1, number2):
    solution = int(number1) + int(number2)
    return solution

"""
def outretries(number1, number2, number3, solution, tries):

*Change outretries to isCorrect(number3, solution, tries)*
this funtion should compare number3 and the solution 
and keep track of tries.
it must return tries to parent function.

"""
def isCorrect(number3, solution, tries):

    if number3 == solution:
            print("Correct Answer: ", solution)
            print("You got it Correct! ")
            tries += 1
            return tries

    while number3 != solution:
        print("You Got it wrong, Try again") 
        print(number3, " / ", solution )
        tries += 1
        number3 = askAnswer() ## number3 ready initizalized (Asked again because it was wrong.)
        if number3 != solution:
            print("You ran out of tries")
            print("Your incorrect answer was: ", number3)
            print("The Correct answer is: ", solution)
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
        ## added for the problem slicing
        equation = askProblem()
        equation = equation.split(" ")
        number1 = equation[0]
        opperation = equation[1]
        number2 = equation[2]
        number3 = int(equation[4])

        solution = getSolutionAdd(number1, number2)
        ## Removed the number1 and number2 in outretries and change name to isCorrect()
        tries = isCorrect(number3, solution, tries)
        store = str(number1) + "/" + str(number2) + "/" + str(solution)
        print(store)
        
        memory.append(store)
    
    print("Tries: ", tries)  

def main():
    print("main module")     

checkerAdd()
