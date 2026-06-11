day = int(input("请输入星期日: "))

match day:
    case 1:
        print("--星期一--")
    case 2:
        print("--星期二--")
    case 3:
        print("--星期三--")
    case 4:
        print("--星期四--")
    case 5:
        print("--星期五--")
    case 6:
        print("--星期六--")
    case 7:
        print("--星期日--")
    case _:
        print("--输入有误!--")

#简易计算器
num1 = float(input("请输入第一个数字: "))
num2 = float(input("请输入第二个数字: "))
oper =input("请输入运算符( + - * / ): ")

match oper:
    case "+":
        print(num1 + num2)
    case "-":
        print(num1 - num2)
    case "*":
        print(num1 * num2)
    case "/":
        if num2 !=0:
            print(num1 / num2)
        else:
            print(" 0不能做被除数! ")
    case _:
        print(" 运算符输入错误! ")

