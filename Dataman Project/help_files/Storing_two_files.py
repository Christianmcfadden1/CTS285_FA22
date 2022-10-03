def main():
    memory = [""]
    displayMem = [""]
    howMany = int(input("how many problems would you like to check: "))
    for i in range(0, howMany):
        equation = askProblem()
        equation = equation.split(" ")
        number1 = equation[0]
        opperation = equation[1]
        number2 = equation[2]
        memory, displayMem, op = checkOperation(number1, number2, opperation, memory, displayMem)
    print(memory)
    print(displayMem)

def storeAdd(number1, number2, memory, op, displayMem):
    print()
    solution = getSolutionAdd(number1, number2)
    store = str(number1) +  " " + op + " " + str(number2) + " " + str(solution)
    print(store)
    memory.append(store)
    displayStore = str(number1) +  " " + op + " " + str(number2)
    print(displayStore)
    displayMem.append(displayStore)
    return memory, displayMem




def checkOperation(number1, number2, opperation, memory, displayMem):
    print()
    if opperation == "+":
        op = opperation
        memory, displayMem = storeAdd(number1, number2, memory, op, displayMem)
        return memory, displayMem, op

    if opperation == "-":
        op = opperation
        memory, tries = storeSubtract(number1, number2, number3, memory, tries, op)
        return memory, tries, op

    if opperation == "*":
        op = opperation
        memory, tries = storeMulti(number1, number2, number3, memory, tries, op)
        return memory, tries, op

    if opperation == "/":
        op = opperation
        memory, tries = storeDivide(number1, number2, number3, memory, tries, op)
        return memory, tries, op

def askProblem():
    guess = input("Please enter your equation (Separate it by spaces): ")
    return guess

def getSolutionAdd(number1, number2):
    solution = int(number1) + int(number2)
    return solution

main()
