#字符串
a = "Python"
b = 'hello'
c='''www'''
print(a,b,c)

# v= 'It's very good'   ---报错,前两个单引号配对了
v= 'It\'s very good'
print(v)

s='''
 各位老板好，新年快乐！
 祝你工作顺利，家和万事兴
 谢谢！
'''
print(s)

#字符串叠加输出以及注意事项
s1 = "人生苦短"
s2 ="嘻嘻哈哈"
print("我的生活:" + s1 +"," +s2)
# --->str(int) 将数字转为字符串
name = "涛哥"
age  = 20

pro = "大数据"
hobby = "python,c++"
print("大家好，我是" + name +", 今年" +str(age)+"岁,学习的专业是" +pro +",爱好" +hobby ) ---->age 为数字类型，在字符串语句中需要转化为字符型

# f"内容{变量名}"
print("大家好，我是%s, 今年%d岁,学习的专业是%s,爱好%s" % (name,age,pro,hobby) )
print(f"大家好，我是{name}, 今年{age}岁,学习的专业是{pro},爱好{hobby}")
