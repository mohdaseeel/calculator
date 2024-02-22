#CALCULATOR

def add(num1 ,num2):
    return num1+num2

def sub(num1 ,num2):
    return num1-num2

def mul(num1 ,num2):
    return num1*num2

def div(num1 ,num2):
    return num1/num2


while True:

    print("CALCULATOR")
    print("1: ADD")
    print("2: SUB")
    print("3: MUL")
    print("4: DIV")
    print("5: INVALID OPTION")

    option = input("Select your Option: 1,2,3,4,5: ")

    if option == '5':
        print("exit the program")
        break
    
    if option in ('1','2','3','4'):
        num1 = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))

        if option == '1':
            print("RESULT: ",add(num1,num2))
        elif option == '2':
            print("RESULT: ",sub(num1,num2))
        elif option == '3':
            print("RESULT: ",mul(num1,num2))
        elif option == '4':
            print("RESULT: ",div(num1,num2))
    else:
        print("INVALID OPTION SELECTED")        
