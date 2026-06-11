"""切片，指对操作的数据截取其中一部分的操作，列表，字符串，元组都支持切片操作
语法:序列数据[开始索引:结果索引:步长]
不包含结束索引位置对应的元素，开始索引默认为0; 结果索引未指定则默认为列表长度，步长默认为1
索引采用正向反向都可以
步长是选取间隔，默认为1
"""
# s = [1,2,3,4,"HELLO",True,666,777,888,"你好"]
# print(s[1::5])
# """
# append()   在列表尾部追加新元素   s.append(12)
# insert()   在指定索引前，插入该元素  s.insert(0,92)
# remove()   移除列表中第一个匹配到的值  s.remove(75)
# pop()      删除列表中指定索引位置的元素(若未指定索引，默认删除最后一个元素)   s.pop(3)
# sort()     对列表进行排序。数据类型一致，才能进行排序  s.sort()
# reverse()  反转列表  s.reverse()
#   """
# s = [1,33,75,77,6,75,666,-1]
# print(s)
#
# s.append(12)
# print(s)
#
# s.insert(0,92)
# print(s)
#
# s.remove(75)
# print(s)
#
# s.pop(3)
# print(s)
#
# s.sort()
# print(s)
#
# s.reverse()
# print(s)
#
# print(s.count(1))
#
list=[]
while True:
    object=input("请输入行业: ")
    if object=="":
        break
    list.append(object)

list.sort
print(list)
