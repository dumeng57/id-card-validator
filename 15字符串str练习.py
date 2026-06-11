#有一个字符串的加密规则按一下步骤进行：

# 原文中所有的字符都在字母表中被循环左移了三个位置（例如 decABC --> abzXYZ）
# 逆序存储（例如 abzXYZ--> ZYXzba ）
# 大小写反转（例如 ZYXzba--> zyxZBA）

# def shift_char(c,n):
#     if 'a'<=c<='z':
#         return chr((ord(c)-ord('a')+n) % 26+ord('a'))
#     elif 'A'<=c<='Z':
#         return chr((ord(c)-ord('A')+n) % 26+ord('A'))    #chr()转回字符，ord()查找字符ASCII码
#
#
#
# str1=input()
# n=3
# str2=""
# result=''
# for i in str1:
#     if 'a'<=i<='z':
#         str2+=i.upper()
#     elif 'A'<=i<='Z':
#         str2+=i.lower()
# for i in str2:
#     result+=shift_char(i,n)
# print(result[::-1])

#统计单词个数
# str1=input()
# word=0
#
# if str1 == "":
#     print("count = 0")
# else:
#     for i in range(len(str1)-1):
#         if (str1[i]!=" ") and (str1[i+1]==" ") :
#             word+=1
#     if str1[-1]!=" ":
#         word+=1
# print(f"count = {word}")

# str1=input()
# str2=""
# num=0
# for i in str1:
#     if i.isalpha():
#         if i.lower() not in str2 and i.upper() not in str2:#加入大小写判断防止一个字母重复计入
#             str2+=i
#     elif i.isdigit():
#         print(i)
#
# if len(str2)>=10:
#     print(str2[:10])
# else:
#     print("not found")
#

# str1=input()
# num1=0
# num2=0
# num3=0
# for i in str1:
#     if i.isalpha():#判断字符是否为字母
#         num1+=1
#     elif i.isdigit():#判断字符是否为数字
#         num2+=1
#     else:
#         num3+=1#判断字符为其他字符
# print(f"英文字母{num1}个，数字字符{num2}个，其他字符{num3}个")

T=int(input())

i=0
strings=[]

while i<T:
    strings.append(input())#把每个字符串存入列表中，在从列表读取每个字符串
    i+=1
for j in strings:
    if j==j[::-1]:#判断是否为回文数
        print("YES")
    else:
        print("NO")
