#set,无序，不重复，可修改
s={100,200,300,400,500,600}
print(s)#--乱序输出
#
   # s1.remove(300)无法改变集合元素

print(s)
s.add(2)
print(s)
#s.clear()
print(s)
s.pop()#--随机删除集合元素
print(s)

s2={"A","B","C","D","E"}
s3={"A","B","g","k","E"}

#A.difference(B),A有但B没有的元素，差集
print(s2.difference(s3))
print(s3.difference(s2))

#AunionB，A与B的并集
print(s2.union(s3))

#Aintersection(B),AB的交集
print(s2.intersection(s3))
