"""
Version 9 (Add feature on memorybank)

Must get problem and store it 
must display problems in memory
After 10 problems game starts to quiz friends.
Must keep track of all correct answers
"""

def askProblem():
    guess = input("Please enter your equation (Separate it by spaces): ")
    return guess

def getSolutionAdd(number1, number2):
    solution = int(number1) + int(number2)
    return solution

def main():
    print()
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
        ## Add if user wants to see the memory of problems entered
    displayBank(displayMem)
    print("what oh its been done before")
    print(memory)
    for i in memory:
        if i == "":
            continue
        equation = i
        equation = equation.split(" ")
        print(equation)
        number1 = equation[0]
        opperation = equation[1]
        number2 = equation[2]
        solution = equation[3]
        correct, tries = askResponse(number1, opperation, number2, solution)
        print(correct, tries)

"""
if number3 == solution:
        print("You got it correct! ")
        print(number3 , solution)
        correct + 1
        return correct
    elif number3 != solution:
        print("Sorry that is incorrect Try again.")
        while tries > 2:
            number3 = int(input("What is your answer? "))
"""
    
def askResponse(number1, opperation, number2, solution):
    print("---------Quiz----------")
    print(" " + str(number1) + " " + str(opperation) + " " + str(number2) + " = ?")
    number3 = int(input("What is your answer? "))
    tries = 1
    correct = 0
    if str(number3) == solution:
            print("Correct Answer: ", solution)
            print("You got it Correct! ")
            correct += 1
            return correct, tries

    while str(number3) != solution:
        print("You Got it wrong, Try again") 
        number3 = askAnswer() 
        if number3 != solution:
            print("You ran out of tries")
            print("Your incorrect answer was: ", number3)
            print("The Correct answer is: ", solution)
            number3 = solution
            tries += 1
            return correct, tries
        if str(number3) == solution:
            print("Correct Answer: ", solution)
            print("You got it Correct! ")
            correct += 1
            tries += 1
            return correct, tries
    

def displayBank(displayMem):
    option = input("Display?")
    if option == "1":
        print()
        displayMem.remove(displayMem[0])
        counter = 1
        for i in displayMem:
            print(str(counter) + ". " + i + " = ?")
            counter += 1
    elif option == "2":
            print("Problems Display Skipped.")
    
def askAnswer():
    number3 = int(input("What your answer: "))
    return number3

"""
def displayBank(displayMem):
    displayMem.remove(displayMem[0])
    counter = 1
    for i in displayMem:
        print(str(counter) + ". " + i + " = ?")
        counter += 1
"""

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

main()