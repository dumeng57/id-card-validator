"""案例1: 根据输入的用户名和密码执行登录操作，具体要求如下:
         1 .正确输入用户名和密码为admun/666888或zhangsan/123456或taoge/888666
         2 .输入的用户名或密码不能为空!
         3 .用户名和密码正确，输出登录成功，进入B站首页~
         4 .用户名和密码不正确，输出用户名或密码错误，请重新输入!
"""
# while True:
#     username=input("请输入正确的用户名: ")
#     password=input("请输入正确的密码: ")
#
#     if username=="" or password=="":
#         print("用户名和密码不能为空 ! 请重新输入")
#         continue
#     elif username =="admun" and password =="666888":
#         print("登录成功，进入B站首页~")
#         break         #使得用户登录成功后程序停止
#     elif username =="zhangsan" and password =="123456":
#         print("登录成功，进入B站首页~")
#         break
#     elif username =="taoge" and password =="888666":
#         print("登录成功，进入B站首页~")
#         break
#     else:
#         print("用户名或密码错误，请重新输入!")
# """
# random
# 1 系统随机生成一个随机数import randomrandom_number = random.randint( a: 1, b: 100 )
# 2 用户根据提示猜数字，并将所猜的数字输入系统
# 3 如果猜错，系统给出提示是猜大了，还是猜小了，然后继续输入猜的数字
# 4 如果猜对，系统自动退出，游戏结束
# """
# import random
# random_num = random.randint(1,100)
#
# while True:
#     num = int(input("请输入一个数字: "))
#     if num < random_num:
#         print("你输入的数字太小了~")
#     elif num > random_num:
#         print("你输入的数字太大了~")
#     else:
#         print("恭喜你，猜对了,666")
#         break
L=int(input())
num=0
sum=0
list=[]

if 1<=L<=1e5:
    for i in range(2,9999):
        for j in range(2,int(i**0.5)+2):
            if j<i and i%j==0:
                break
            else:
                sum=sum+i
                if sum<=L:
                    list.append(i)
                    num+=1
                    continue
for i in list:
    print(i)
print(num)

