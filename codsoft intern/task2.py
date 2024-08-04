#Simple Calculator with basic arithmetic operations

firstno = int(input("Enter the first number : "))
secondno = int(input("Enter the second number : "))
operation = input("Enter any operation among these + , - , * , / : ")

if (operation == "+") :
    result = firstno + secondno
elif (operation == "-"):
    result = firstno - secondno
elif (operation == "*"):
    result = firstno * secondno
else :
    result = firstno / secondno

print(result)