def calculator(num1, num2, op):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        return num1 / num2



while True:
    num1 = int(input("첫 번째 숫자 입력\n"))
    if num1 == 0:
        print("계산기를 종료합니다.")
        break
    op = input("연산자 입력\n")
    num2 = int(input("두 번째 숫자 입력\n"))
    result = calculator(calculator(num1, num2, op), num3, op2)
    print("계산 결과: " + str(result))