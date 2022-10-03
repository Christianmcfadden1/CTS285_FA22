"""
Version 8 (Adding Division feature)

In this version i will be taking all the opperator 
features and adding it to the same spell checker file.

**I will need to change the equation by spaces so that 
it will not interfere with the / in division**

**Also adding a feature to the program where it 
creates a list to deminstrate the problem you have entered.**
"""
def getSolutionAdd(number1, number2):
    solution = int(number1) + int(number2)
    return solution

def checkerAdd(number1, number2, number3, memory, tries, op):
    solution = getSolutionAdd(number1, number2)
    ## Removed the number1 and number2 in outretries and change name to isCorrect()
    tries = isCorrect(number3, solution, tries)
    store = str(number1) +  " " + op + " " + str(number2) + " " + str(solution)
    print(store)
    memory.append(store)
    return memory, tries

"""
def getSolutionMulti(number1, number2):
    Changing function name to getSolutionDivide(number1, number2)
    also changing the opperator from "*" to "/"
"""
def getSolutionDivide(number1, number2):
    solution = int(number1) / int(number2)
    return solution

"""
def checkerMulti(number1, number2, number3, memory, tries, op):
Changing function name to checkerDivide(number1, number2, number3, memory, tries)
"""
def checkerDivide(number1, number2, number3, memory, tries, op): ## it is important to store the opperation in memory.
    solution = getSolutionDivide(number1, number2)
    tries = isCorrect(number3, solution, tries)
    store = str(number1) + " " + op + " " + str(number2) + " " + str(solution)
    print(store)
    memory.append(store)
    return memory, tries

"""
def getSolutionSubtract(number1, number2):
    Changing function name to getSolutionMulti(number1, number2)
    also changing the opperator from "-" to "*"
"""
def getSolutionMulti(number1, number2):
    solution = int(number1) * int(number2)
    return solution

"""
def checkerSubtract(number1, number2, number3, memory, tries, op):
    Changing function name to checkerMulti(number1, number2, number3, memory, tries)
"""
def checkerMulti(number1, number2, number3, memory, tries, op): ## it is important to store the opperation in memory.
    solution = getSolutionMulti(number1, number2)
    tries = isCorrect(number3, solution, tries)
    store = str(number1) + " " + op + " " + str(number2) + " " + str(solution)
    print(store)
    memory.append(store)
    return memory, tries

"""
def getSolutionAdd(number1, number2):
    Changing function name to getSolutionSubtract(number1, number2)
    also changing the opperator from "+" to "-"
"""
def getSolutionSubtract(number1, number2):
    solution = int(number1) - int(number2)
    return solution

"""
def checkerAdd(number1, number2, number3, memory, tries):
    Changing function name to checkerSubtract(number1, number2, number3, memory, tries)
"""
def checkerSubtract(number1, number2, number3, memory, tries, op): ## it is important to store the opperation in memory.
    solution = getSolutionSubtract(number1, number2)
    tries = isCorrect(number3, solution, tries)
    store = str(number1) + " " + op + " " + str(number2) + " " + str(solution)
    print(store)
    memory.append(store)
    return memory, tries

## not nessary
def askProblem():
    guess = input("Please enter your equation (Separate it by spaces): ")
    return guess

## not nessary
def askAnswer():
    number3 = int(input("What your answer: "))
    return number3

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
        memory, tries = checkerDivide(number1, number2, number3, memory, tries, op)
        return memory, tries, op

def whatIsOp(op):
    if op == "+":
        op = "Addition"
        return op
    if op == "-":
        op = "Subtraction"
        return op
    if op == "*":
        op = "Multiplication"
        return op
    if op == "/":
        op = "Division"
        return op

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
    name = whatIsOp(opperation)
    counter = 0
    for i in memory:
        cut = i
        counter += 1
        print(str(counter) + ". " + str(name))
        wow = cut.split(" ")
        number1 = wow[0]
        opperation = wow[1]
        number2 = wow[2]
        number3 = wow[3]
        print("---- " + number1 + " " + opperation + " " + number2 + " " + "=" + " " + number3)


main()
