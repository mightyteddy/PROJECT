class Calculator:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def plus(self):
        print(first + " + " + second + " = " + str(int(first) + int(second)))
    def minus(self):
        print(first + " - " + second + " = " + str(int(first) - int(second)))
    def multiply(self):
        print(first + " * " + second + " = " + str(int(first) * int(second)))
    def divide  (self):
        print(first + " / " + second + " = " + str(int(first) / int(second)))

yourNum = input("사칙연산 때릴 수 두개 입력\n")
yourNum = yourNum.split(" ")
first = yourNum[0]
second = yourNum[1]

math = Calculator(first, second)
math.plus()
math.minus()
math.multiply()
math.divide()






