#字典--dict--
#dict={(key:value)}---键值对类型,key不能重复，key必须是不可变类型，像(str,int,float,tuple
name_list=["王林，“韩立","李沐晚"]
score_list=[670,580,480]
dict1={"王林":670,"韩立":580,"李沐晚":480}
print(dict1)

#值=字典名称[key]
score=dict1["李沐晚"]
print(score)
print(type(dict1))

dic2={(0,0):670,1:580,2:480}
print(dic2)

print(dict1["李沐晚"])
dict1["李沐晚"]=680
print(dict1["李沐晚"])#--字典的值可更改

# --添加
dict1["李大哥"]=120
print(dict1)

#删除
# dict1.pop("李沐晚")
# print(dict1)
#
# del dict1["李大哥"]
# print(dict1)

# print(dict1.get("韩立"))
# print(dict1.keys())
# print(dict1.values())
# print(dict1.items())

#--遍历
# for k in dict1.values():
#
#
# for item in dict1.items():
#     print(f"{item[0]}: {item[1]}")
dict1={"王林":670,"韩立":580,"李沐晚":480}
dict2={"王林":670,"韩立":580,"李沐晚":480}
list1=[]
print(list1(*dict1,*dict2))