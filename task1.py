while True:

    num1 = float(input("Enter Number 1:"))
    num2 = float(input("Enter Number 2:"))

    operation = input("Enter Operation (+,-,*,/):")

    if(operation == "+"):
        print("Result:",num1+num2)
    
    elif(operation == "-"):
        print("Result:",num1-num2)

    elif(operation == "*"):
        print("Result:",num1*num2)

    elif(operation == "/"):
        if(num2 !=0):
         print("Result:",num1/num2)
        else:
            print("Cannot be divided by zero")

    else: 
     print("Invalid Operation")

    cont = input("Do you want to continue?:(y/n)")
    if cont.lower() != "y" :
        break