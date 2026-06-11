# 案例1，将用户输入的10个数字，存储到一个列表中，并将列表中的数字进行排序，输出其中的最小值，最大值

#1.定义空列表
# # num_list = []
#
# #用户输入10个数字并存入列表
# for i in range(10):
#     num = int(input("请输入一个有效的数字: "))
#     num_list.append(num)
#
# print("数字列表: ",num_list)
#
# num_list.sort()
# print("排序后的数字列表: ",num_list)
#
# print("列表元素的最大值: ",num_list[-1])
# print("列表元素的最小值: ",num_list[0])
# print("平均值: ",sum(num_list)/len(num_list))
#
#
# #案例2，将两个列表合并，并去除重复项
#
# num_list1=[1,33,23,53,77,64,81,3,123,444,97]
# num_list2=[22,48,57,64,23,46,88,100,33]
#
# 合并方法1
# for num in num_list2:
#     num_list1.append(num)
# print("合并后的列表为: ",num_list1)
#
# # 2解包操作:将容器拆解成独立的元素
# # 组包: 将多个值合并到一个容器当中
# num_list=[*num_list1,*num_list2]
# print("合并后的列表为: ",num_list)
#
# #3直接合并
# num_list = num_list1 + num_list2
# print("合并后的列表为: ",num_list)
#
# #去除重复项
# num_list3=[]
# for num in num_list:
#     if num not in num_list3:
#         num_list3.append(num)
# print("去除重复项后的列表为: ",num_list3)
#
# """案例3
# 生成1-20平方的列表
# 在此列表基础上找到偶数，并把他们的平方组成新的列表
# """
# num_list1=[]
# num_list2=[]
# #法1，循环生成数字
# for i in range(1,21):
#     num_list1.append(i**2)
# print(num_list1)
# for num in num_list1:
#     if num%2==0:
#         num_list2.append(num**2)
# print(num_list2)
# #法2，列表推导式
# # 格式1[要插入的值 for i in 序列或列表]
# # 格式2[要插入的值 for i in 列表if条件]
# num_list3=[i**2 for i in range(1,21)]
# print(num_list3)
# num_list4=[i**2 for i in num_list3 if i%2==0]
# print(num_list4)

#下述程序从键盘读入多个以逗号分隔的元素并将其组织在一个列表中，然后遍历列表删除其中重复的元素。具体地，假设列表中存在k个值为a的元素，删除前k-1个元素，保留最后一个，不同元素在列表中的相对位置不应被改变。
# v = list(eval(input()))
# print("before:",v)
#
# for x in v:
#     cnt = v.count(x)
#     if cnt >= 2:
#         for i in range(cnt-1):
#             v.remove(x)
#
# print("after:",v)

# v = list(eval(input()))#录入列表
# print("before:",v)#打印原列表
# v1=[]#创造一个空列表为后续从后往前录入列表元素做准备
#
# for i in v[::-1]:
#     if i not in v1:
#         v1.append(i)  #这里实现只保留重复元素的最后一个序列，且避免了python系统中True被当成1来使用，而是直接把True当成字符串来加入新列表，最终实现正常运行
# print("after:",v1[::-1])  #打印筛选后的列表

def f(n,k):
    list1=list(range(1,n+1))
    for i in range(0,len(list1),3):
        list1.remove(list1[i])
    return list1


n=int(input())
k=int(input())
print(f(n,k))



