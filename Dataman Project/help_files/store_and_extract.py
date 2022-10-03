memory = [""]
number1 = int(input("#1: "))
number2 = int(input("#2: "))
solution = number1 + number2

store = str(number1) + "/" + str(number2) + "/" + str(solution)
print(store)
memory.append(store)
print(memory)

this = memory[1].split("/")
print(this)
print(this[0] + " + " + this[1] + " = " + this[2])


