"""
Version 6 (Adding Multiplication feature)

In this version i will be taking the Subtraction feature 
code and converting it to Multiplication feature.
I will also be choose which functions are nessary.
"""

## not nessary

def askProblem():
    guess = input("Please enter your equation (Separate it by spaces): ")
    return guess

## not nessary

def askAnswer():
    number3 = int(input("What your answer: "))
    return number3

"""
def getSolutionSubtract(number1, number2):
    Changing function name to getSolutionMulti(number1, number2)
    also changing the opperator from "-" to "*"
"""

def getSolutionMulti(number1, number2):
    solution = int(number1) * int(number2)
    return solution

## Not nessary

def isCorrect(number3, solution, tries):

    if number3 == solution:
            print("Correct Answer: ", solution)
            print("You got it Correct! ")
            
            return tries

    while number3 != solution:
        print("You Got it wrong, Try again") 
        number3 = askAnswer() 
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

"""
def checkerSubtract(number1, number2, number3, memory, tries, op):
    Changing function name to checkerMulti(number1, number2, number3, memory, tries)
"""

def checkerMulti(number1, number2, number3, memory, tries, op): ## it is important to store the opperation in memory.
    solution = getSolutionMulti(number1, number2)
    tries = isCorrect(number3, solution, tries)
    store = str(number1) + "/" + op + "/" + str(number2) + "/" + str(solution)
    print(store)
    memory.append(store)
    return memory, tries

def checkOp(number1, number2, number3, opperation, memory, tries):
    print()
    if opperation == "+":
        op = opperation
        print("Addition")
        memory, tries = checkerAdd(number1, number2, number3, memory, tries, op)
        return memory, tries, op

    ## i passed op to checker and 

    if opperation == "-":
        op = opperation
        print("Subtraction")
        memory, tries = checkerSubtract(number1, number2, number3, memory, tries, op)
        return memory, tries, op

    if opperation == "*":
        op = opperation
        print("Multiplication")
        memory, tries = checkerMulti(number1, number2, number3, memory, tries, op)
        return memory, tries, op

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
     
    print("Retries: ", tries) 
    memory.remove(memory[0])
    print(memory)

main()
