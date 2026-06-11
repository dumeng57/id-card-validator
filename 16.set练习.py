s=set(map(int,input().split(",")))
s1={1,2,3,4,5}
s2={6,7,8,9,10}
print(s2-s)
list1=[*(s2-s)]
list1.sort()
print(*list1)