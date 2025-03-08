class Calculator:
    def __init__(self):
        pass
    def add(self,x,y):
        return x+y
    def sub(self,x,y):
        return x-y
    def mult(self,x,y):
        return x*y
    def div(self,x,y):
        if y == 0:
            return "Error! Division by zero."
        return x / y
    def square(self,n):
        return n*n
    def cube(self,n):
        return n*n*n
    def sqrt(self,n):
        return n**(1/2)
    def option(self):
        while(True):
            print("Operation Choice :")
            print("1 -> Addition")
            print("2 -> Subtraction")
            print("3 -> Multiplication")
            print("4 -> Division")
            print("5 -> Square")
            print("6 -> Cube")
            print("7 -> Square Root")
            print("8 -> Exit")
            try:
                opt=int(input("Enter Your Choice : "))
                if(opt==1):
                    x=int(input("Enter the First Number for addition : "))
                    y=int(input("Enter the Second Number for addition : "))
                    print("Result :", self.add(x, y))
                elif(opt==2):
                    x=int(input("Enter the First Number for subtraction : "))
                    y=int(input("Enter the Second Number for subtraction : "))
                    print("Result :", self.sub(x, y))
                elif(opt==3):
                    x=int(input("Enter the First Number for multiplication : "))
                    y=int(input("Enter the Second Number for multiplication : "))
                    print("Result :", self.mult(x, y))
                elif(opt==4):
                    x=int(input("Enter the First Number for division : "))
                    y=int(input("Enter the Second Number for division : "))
                    print("Result :", self.div(x, y))
                elif(opt==5):
                    n=int(input("Enter the Number for square : "))
                    print("Result :",self.square(n))
                elif(opt==6):
                    n=int(input("Enter the Number for cube : "))
                    print("Result :",self.cube(n))
                elif(opt==7):
                    n=int(input("Enter the Number for square root : "))
                    print("Result :",self.sqrt(n))
                elif(opt==8):
                    exit()
            except ValueError:
                print("Invalid input! Please enter a valid number.")
calc=Calculator()
calc.option()




