def plusFunc(firstNum, secondNum):
    return firstNum + secondNum


def minusFunc(firstNum, secondNum):
    return firstNum - secondNum


def multiplyFunc(firstNum, secondNum):
    return firstNum * secondNum


def divFunc(firstNum, secondNum):
    return firstNum / secondNum


def mainFunc():
    boolForGlobalWhile = 1
    boolForChoosingOperation = 1

    print("Welcome To Calculator\n")

    while boolForGlobalWhile > 0:

        try:
            firstNum = float(input("Enter First Num: "))
            secondNum = float(input("Enter Second Num: "))
        except:
            print("Redneck, Enter A Number!\n")
            continue

        while boolForChoosingOperation > 0:
            operation = input("Enter operation (+, -, *, /): ")
            print("\n")
            if operation == "+":
                print(firstNum, " + ", secondNum, " = ", plusFunc(firstNum, secondNum), " \n ")
                break
            if operation == "-":
                print(firstNum, " - ", secondNum, " = ", minusFunc(firstNum, secondNum), " \n ")
                break
            if operation == "*":
                print(firstNum, " * ", secondNum, " = ", multiplyFunc(firstNum, secondNum), " \n ")
                break
            if operation == "/":
                if secondNum == 0:
                    print("Division By Zero Not Allowed!\n")
                    break
                print(firstNum, " / ", secondNum, " = ", divFunc(firstNum, secondNum), " \n ")
                break
            else:
                print("Redneck, Enter Correct Operation!\n")
                boolForChoosingOperation = 1

        print("Are You Want To Continue?")
        print("1 - Continue")
        print("Otherwise - No\n")
        wannaContinue = input("Your Choice: ")
        print("\n")

        if wannaContinue == "1":
            boolForGlobalWhile = 1
            boolForChoosingOperation = 1
        else:
            print("See Ya.")
            boolForGlobalWhile = 0
            boolForChoosingOperation = 0


mainFunc()
