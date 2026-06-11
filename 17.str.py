# str1="sdjaddadkadact"
#
# str2="act"
# if str1.find(str2)>0:
#     print("YES")
# else:
#     print("NO")       #--查找字符
#

# str1=input()
# str2=input()
# for i in str1:
#     if i in str2:
#         if i == str1[-1]:
#             print("yes")
#         else:
#             continue
#     else:
#         print("no")
#         break
list1=list(range(1,6))
print(list1)
list1.pop(0)
list1.append(1)

str = input()   #录入字符串
num = 0       #记录字符串中的空格字符
for i in str:  #循环找出空格个数
    if i == " ":
        num += 1

word = len(str.split())  #取字符串单词个数，原理是取字符串长度以空格为一个字符
print(f"{word},{(len(str) - num) / word:.2f}")

#身份证检验
def turn(n):
    list3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]          #记录余数可能取值   这部分可以去除
    list4 = [1, 0, "X", 9, 8, 7, 6, 5, 4, 3, 2]         #给出余数对应检验码
    posit = list3.index(n)                              #查找对应检验码
    return list4[posit]                                 #返回检验码


str1 = input().strip()                              #用户输入身份证
if len(str1) != 18 :                         #检验身份证是否正确前提
    print("错误")
else:
    s = 0                           #   用来权方求和

    list1 = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]           #对应权方值
    list2 = []

    for i in str1[:-1]:
        list2.append(int(i))                     #对前17位数字记录
    for i in range(17):
        s = s + list2[i] * list1[i]             #每个数字乘对应权方值，并求和
    Z = s % 11                                  #求和之后的权方取余得到基础检验码

    expect = turn(Z)                    #单独为检验码定义，便于后续转化字符，避免字符转化的表述问题
    if str(expect) == str1[-1].upper:             #判断身份证最后一位检验码是否抄录成功
        print("正确")             #抄录成功返回正确
    else:
        print("错误")             #抄录错误返回错误

