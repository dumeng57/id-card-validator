# n=int(input())
# for i in range(n//3+1):
#     if (n-3*i)>=0:
#         for j in range((n-3*i)//2+1):
#             if (n-3*i-j*2)>=0:
#                 if (i+j+(n-3*i-j*2)*2)==20:
#                     print(f"{i} {j} {(n-3*i-j*2)*2}")
#                 else:
#                     continue
#             else:
#                 if (i+(n-3*i)*2)==20:
#                     print(f"{i} {j} {(n-3*i)*2}")
#     else:
#         for j in range(n//2+1):
#             if n-2*j > 0:
#                 if (j+(n-2*j)*2)==20:
#                     print(f"0 {j} {(n-j*2)*2}")




# n=int(input())
#
# if 8<=n<=1000:
#     for i in range(n//3+1):
#         big=i
#         for j in range((n-3*big)//2+1):
#             mediu=j
#             small=(n-3*big-2*mediu)*2
#             if (big+mediu+small) == n:
#                 print(f"{big} {mediu} {small}")

# dict1=input()
# dict2=input()
# print(dict1)
# print(dict2)

# str1=input()
# # print(str1)
# list1=list(map(int,input().split()))
# list2=list(map(int,input().split()))
# list3=[]
# for i in list1:
#     if i not in list2:
#         list3.append(i)
# for i in list2:
#     if i not in list1:
#         list3.append(i)
# print(list3)



# str=input().strip()
# c=input()
# if c.upper() in str :
#     print(f"result: {str.replace(c.upper(),'')}")
# elif c.lower() in str :
#     print(f"result: {str.replace(c.lower(),'')}")
# else:
#     print(f"result: {str}")

# n=int(input())  #录入数据

# go_=set(input().split())   #录入赌神拿走的牌
# back=set(input().split())  #录入赌圣拿回来的牌
#
# list3=[]
# list4=[*(go_-back)]
# fina=[]
# list1=["r","g","b"]    #录入花色种类
# list2=list(range(1,n+1))   #记录花色的序列
#
# for i in list1:
#     for j in list2:
#         list3.append(i+str(j))   #创建列表记录每一种花色及其序列
# for i in list3:
#     if i not in list4:
#         fina.append(i)   #把除了被拿走的加入fina列表
# for i in fina:
#     print(i)

# list1=[]
#
# while True:     #循环实现录入字符串，知道遇见字符'q'
#     k=input()
#     if k=="q":
#         break
#     else:
#         list1.append(k)
# for i in range(len(list1)-1):          #寻找字符出现次数最多的那个字符，并把他移到最后一个位置
#     if list1.count(list1[i])>list1.count(list1[i+1]):
#         list1[i],list1[i+1]=list1[i+1],list1[i]
# print(list1[-1],list1.count(list1[-1]))



# T=int(input())
# s=0
#
# for i in range(T):
#     day,k=map(int,input().split())
# j=(k+2)*(2**(day-1))-2
# print(j)


str="aaa bbb ccccccccccc"
word=(len(str))/3
print(f"{word:.2f}")



