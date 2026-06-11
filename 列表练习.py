# v,m,n=map(int,input().split(","))
#
# if v+m>0 and n>=0 and m>n:
#     s=0
#     s1=0
#     day=1
#     while (s1<v):
#         s=s1+m
#         if s>=v:
#             print(day)
#             break
#         s1=s-n
#         day+=1
# else:
#     print("Valid")
# money = int (input())
# num=0
# if (money//20)>=1:
#     for n20 in range(money//20,-1,-1):
#         s1=money-20*n20
#         if (s1//10)>=1:
#             for n10 in range(s1//10,-1,-1):
#                 s2=s1-10*n10
#                 if (s2//5)>=1:
#                     for n5 in range(s2//5,-1,-1):
#                         s3=s2-5*n5
#                         if (s3//1)>=1 and n5>=1 and n10>=1 and n20>=1 :
#                             print(f"可换得1元{s3}张，5元{n5}张，10元{n10}张，20元{n20}张")
#                             num+=1
#                         else:
#                             continue
#                 else:
#                     continue
#         else:
#             continue
# else:
#     print("Invalid")
# print(f"共{num}种方案")

# num_list=list(input())
#
# for i in range(3,7):
#     num_list[i]="*"
# print(*num_list,sep="")

# str=input()
# str.lower()
# print(str.lower())
#
# for i in str:
#     if 'A'<=i<='Z':
#         None
#
# if len(str)>5:
#     print(str[:5])
# else:
#     print(str)
# list=[]
# for i in range(10):
#     list.append(i)
# print(list)

# def f(n):
#     list1=[]
#     for i in range(1,n+1):
#         if i==1 or i==2:
#             list1.append(int(1))
#         elif i>=3:
#             s=int(list1[i-2])+int(list1[i-3])
#             list1.append(s)
#     print(list1)
#
# n = int(input())
# f(n)

n=int(input())
num=0

for i in range(1,n+1):
    v=list(map(int,input().split()))
    for j in range(len(v)):
        if int(v[j])<60:
            continue
        elif j==len(v)-1:
            num+=1
print(num)
