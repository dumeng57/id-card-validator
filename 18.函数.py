# def f(r,pi):
#     """
#
#     根据圆的半径计算圆的面积和周长
#     :param r: 圆的半径
#     :param pi :圆周率
#     :return :圆的面积，圆的周长
#     """
#     return round(pi*r**2,2),round(2*pi*r,1)
#
# pi=3.14
# print (f(3,3.14))
# area,len=f(3,3.14)
# print(area,len)
# help(f)
#
# def fun_a():
#     print("a...before")
#     fun_b()
#     print("a...after")
#
# def fun_b():
#     print("b...before")
#     fun_c()
#     print("b...after")
# def fun_c():
#     print("c...")
#
# fun_a()
#
# num=1
# def fun_d():
#     global num#----要改变全局变量需要提前说明
#
#     num=100
#     print(num)
# fun_d()
# print(num)

def reg_stu(name,age,gender,city):
    print(f"注册成功，姓名:{name}，年龄：{age}，性别:{gender}，城市：{city}")
    return {"name":name, "age":age,"gender":gender,"city":city}

stu=reg_stu("张三",18,"男","北京")
print(stu)