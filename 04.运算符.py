# 算术运算符 + - * / // ** %
print("10+4 = ",10+4)
print("10-4 = ",10-4)
print("10*4 = ",10*4)
print("10/4 = ",10/4)
print("10//4 = ",10//4)
print("10**4 = ",10**4)
print("10%4 = ",10%4)

#算术运算符的优先级-->** --> * / // %
print("0.1 + 10/4**2 = ",0.1 + 10/4**2)#--->0.725

x = int(input("请输入x的值"))
y=int(input("请输入y的值"))
print("x+y = ",x+y)
print("x-y = ",x-y)

x = float(input("请输入x的值"))  --- 0.5
y= float(input("请输入y的值"))  ---- 0.4
print("x+y = ",x+y)
print("x-y = ",x-y)--> 0.09999999999999998二进制精度损失

# 赋值运算
num = 85
num += 10
print("num += 10后，num = ",num)

num -= 10
print("num-= 10后，num = ",num)

num *= 10
print("num *= 10后，num = ",num)

num //=10
print("num //= 10后，num = ",num)

num %=10
print("num %= 10后，num = ",num)

num **=10
print("num **= 10后，num = ",num)

num /=10
print("num /= 10后，num = ",num)


num = int(input ("请输入一个整数"))
print(f"{num}在10-20之间",num >=10 and num <=20)
print(f"{num}在10-20之间",num <10 or num >20)



