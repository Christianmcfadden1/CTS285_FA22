"""
Version 4

In this version i completed the input of the equations and answer to be spliced.
and store the equation and answer in the memory. program must get the 
opperation from the equation separated by " " 
this version is ready for other features.
"""

def askProblem():
    guess = input("Please enter your equation (Separate it by spaces): ")
    return guess

def askAnswer():
    number3 = int(input("What your answer: "))
    return number3

def getSolutionAdd(number1, number2):
    solution = int(number1) + int(number2)
    return solution

def isCorrect(number3, solution, tries):

    if number3 == solution:
            print("Correct Answer: ", solution)
            print("You got it Correct! ")
            tries += 1
            return tries

    while number3 != solution:
        print("You Got it wrong, Try again") 
        ## print(number3, " / ", solution )
        ## tries += 1
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

def checkerAdd(number1, number2, number3, memory, tries):
    solution = getSolutionAdd(number1, number2)
    ## Removed the number1 and number2 in outretries and change name to isCorrect()
    tries = isCorrect(number3, solution, tries)
    store = str(number1) + "/" + str(number2) + "/" + str(solution)
    print(store)
    memory.append(store)
    return memory, tries

def checkOp(number1, number2, number3, opperation, memory, tries):
    print()
    if opperation == "+":
        op = opperation
        print("Addition")
        memory, tries = checkerAdd(number1, number2, number3, memory, tries)
        return memory, tries, op

    if opperation == "-":
        op = opperation
        print("Subtraction")
        print("not added yet")
    if opperation == "*":
        op = opperation
        print("Multiplication")
        print("not added yet")
    if opperation == "/":
        op = opperation
        print("Division")
        print("not added yet")

def main():
    print("main module") 

    howMany = int(input("how many problems would you like to check: "))
    memory = [""]
    tries = 0
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
        memory, tri, op = checkOp(number1, number2, number3, opperation, memory, tries)   
        tries += tri 
    print("Tries: ", tries) 
    memory.remove(memory[0])
    print(memory)

main()
