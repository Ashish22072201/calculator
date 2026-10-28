def add(a,b):
    return a + b 


def subtract(a,b):
    return a - b 

def multiply(a,b):
    return a * b

def divide(a,b):
    if b == 0:
        raise ValueError("Cannot divide  by Zero")
    return a / b 

def main():
    print("=== Ashish's Calculator ===")

    a = float(input("Enter the first number :"))
    operator = input("Choose Operation(+,-,*,/): ")
    b = float(input("Enter the second number : "))

    if operator == "+":
        result = add(a,b)

    elif operator == "-":
        result = subtract(a,b)

    elif operator == "*":
        result = multiply(a,b)

    elif operator == "/":
        if b == 0:
            print("Error : Cannot Divide by Zero")
            return 
        result = divide(a,b)
    else:
        print("Invalid operator !")
        return

    print("Result: ",result)


if __name__ == "__main__":
    main()