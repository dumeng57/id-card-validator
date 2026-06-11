# 元组基本操作---元素可以重复，不可修改，有序，用于查询

# t1=(80,79,66,1,2222,33,66,5)
#
# print(t1)
# print(type(t1))
#
# #索引访问--跟列表一样
# print(t1[0])
# print(t1[1])
#
# #切片
# print(t1[2:6])
#
# # count()统计元素个数
# print(t1.count(66))
#
# #index()查询元素序列位置
# print(t1.index(80))
#
# #注意点。如果定义单元素的元组，单个元素之间要加逗号，如（100，）
# t2=()
# print(t2)
# t3=(100,)
# print(type(t3))
#
#组包'
t1=(1,2,3,4,5,6,7,8)
t2=1,2,3,4,5,6,7,8

# print(t1)
# print(t2)
#
# #解包
# a,b,c,d,e,f,g,h=t1
# print(a,b,c,d,e,f,g,h)
#
# *a,b,c=t1
# print(a,b,c)
#
# a,*b,c=t1
# print(a,b,c)

a,b,*c,=t1
print(a,b,c)

#交换数字
a=10
b=20
#
# a,b=b,a
# print(a,b)

t=b,a
a,b=t
print(a,b)