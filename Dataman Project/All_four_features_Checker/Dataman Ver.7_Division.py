"""
Version 7 (Adding Division feature)

In this version i will be taking the Multiplication feature 
code and converting it to Division feature.
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
        memory, tries = checkerDivide(number1, number2, number3, memory, tries, op)
        return memory, tries, op

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
