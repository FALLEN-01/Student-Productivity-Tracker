a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
print("Enter your choice: ")
ch=int(input("Enter your choice: "))

if ch==1:
    print("Sum: ",a+b)
elif ch==2:
    print("Difference: ",a-b)
elif ch==3:
    print("Product: ",a*b)
elif ch==4:
    if b != 0:
        print("Quotient: ",a/b)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid choice!")