num1=float(input("enter ur first value"))
op=input("input any operation u want to perform between two values")
num2=float(input("enter ur second value"))
if op=="+":
    print(num1 + num2)
elif op=="*":
    print(num1 * num2)
elif op=="/":
    print(num1 / num2)
elif op=="-":
    print(num1 - num2)
else: 
    print("please enter a valid operatpr")