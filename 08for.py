#遍历字符串

msg = "HELLO WORLD!"
i = 0
for i in msg:
    print(i)

msg = input("Enter your message: ")
for i in msg:
    print(i)
else:
    print("Goodbye")

#1-100奇数之和     注意range(star,end)不包含end,range(end),range(star,end,step)step为间隔
i=0
total = 0
for i in range(1,101):
    if i%2!=0:
        total = total + i
    i = i + 1
print(total)
100-500中3的倍数之和
total = 0
for i in range (100,501):
    if i % 3 == 0:
        total = total + i
print(total)

"""输出一个长方形 m*n
***********....
*********...
"""
m=int(input("请输入长方形的长: "))
n=int(input("请输入长方形的宽: "))

for i in range(n):  #控制行
    for i in range(m):  #控制列
        print("* ",end=" ")
    print()

#打印9*9乘法表
n=1
for i in range(1,10):
    if n ==10:
        break
    for j in range(1,i+1):
        print(f"{j}*{i} = {j*i}",end="\t ")
    print()
