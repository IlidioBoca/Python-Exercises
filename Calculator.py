
def sum(a, b):
        return a + b
def subtraction(a, b):
        return a - b
def multiplication(a, b):
        return a * b
def division(a, b):
    if b!=0:
     return a/b
    else:
      return "Error: division by zero"

print("calculator")
print("1 - Addition")
print("2 - Subtraction")
print("3 - Multiplication")
print("4 - Divisin")

opcao = input("Choose an option:")

a = float(input("Enter the first number:"))
b = float(input("Enter the second number:"))

if opcao == "1":
    print("Result:", sum(a,b))
elif opcao == "2":
    print("Result:", subtraction(a,b))
elif opcao == "3":
    print("Result:", multiplication(a,b))
elif opcao == "4":
    print("Result:", division(a,b))
else:
    print("invalid option!")
