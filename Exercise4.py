print("Select Operation 1.(+) 2.(-) 3.(*) 4.(/)")
Operation = int(input("Select"))

if Operation <= 4 and Operation > 0:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    if Operation == 1:
        print(f"{num1} + {num2} = {(num1)+(num2)}")
    elif Operation == 2:
        print(f"{num1} - {num2} = {(num1)-(num2)}")
    elif Operation == 3:
        print(f"{num1} x {num2} = {(num1)*(num2)}")
    elif Operation == 4:
        print(f"{num1} / {num2} = {(num1)/(num2)}")
else:
    print("Invalid operation selected")