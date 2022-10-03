
equation = input("Please enter your equation (Separate it by spaces): ")
print(equation)
##guess.remove(guess[0])
equation = equation.split(" ")
print(equation)

number1 = equation[0]
opperation = equation[1]
number2 = equation[2]
number3 = equation[4]

print(number1, opperation, number2, "=", number3)
