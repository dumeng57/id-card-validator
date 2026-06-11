#
# ture_account = "18888888888"
# true_password = "666888"
# #开始与用户交互
#
# account=input("请输入您的账号: ")
# password = input("请输入您的密码: ")
#
# if account == ture_account and password == true_password:
#     print("登录成功~")
#     print("进入B站首页 ~")
# else:
#     print("登录失败!")
#     print("账号或者密码错误!")
#
# year = int(input("请输入需要判定的年份: "))
# if (year % 400 == 0) or (year % 100 == 0 and year % 4 == 0):
#     print(f"{year}是闰年~")
# else:
#     print(f"{year}是平年~")
#
# num = int(input("请输入一个数字: "))
#
# #if。。。elif..else..if
# if 成功执行之后elif和else不会执行,只有if 没有执行的时候才继续进行之后的条件判断
#
# if num > 0:
#     print("这是一个正数~")
# elif num < 0:
#     print("这是一个负数~")
# else:
#     print("这是0~")
#
# a,b,c = map(int, input("请输入三角形三边长: ").split())
# if a+b>c and a+c>b and b+c>a:
#     if a==b==c:
#         print(" 这个三角形是等边三角形~ ")
#     elif a==b or a==c or b==c:
#         print(" 这个三角形是等腰三角形~ ")
#     elif a**2+b**2==c**2 or a**2+c**2==b**2 or a**2+c**2==b**2:
#         print(" 这个三角形是直角三角形~ ")
#     else:
#         print(" 这个三角形是普通三角形~ ")
# else:
#     print(f"{ a} {b} {c} 这三边长不能构成三角形!")

#判断一个数字是否为质数
L=int(input())
list1=[]
if L==1:
    print(0)
elif 100000>=L>=2:
    for i in range (2,L+1):
        for j in range(2,i+1):
            if  j<i and i%j==0:
                break
            elif j==i:
                if sum(list1)+i<=L:
                    list1.append(i)
                    print(i)
                    break
        if sum(list1)+i>L:
            break
    print(len(list1))
