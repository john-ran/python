import copy
names = ["john","lol","RNG",["lpl","omg"],"jack","tom"]
print(names[1:-1:2])#这个时候不包括-1即最后一个元素的
#name1 = copy.deepcopy(names)#深copy之后name1就是一个单独的内存空间了
#浅copy的用途,创建联合账户
person = ["name",["sal","100"]]
p1=person[:]
p2=person[:]
p1[0]="lpl"
p2[0]="fengjie"
p1[1][1]=50
p2[1][1]=60
print(p1,p2)
'''name1=names[:]
name2=list(names)
name3=copy.copy(person)
#name1 = copy.copy(names)#复制一个list,列表中的列表在内存中放的是一个指针不是内容，但导致如果内列表的内容发生改，那么cpoy的列表内容也会改变，复制的是内列表的地址
#range(1,10,2)
for i in names:
    print(i)
print(names)
print(name1)
names[2] = "中文"
names[3][0] = "nihao"
print(names)
print(name1)
name1[3][0] = "LPL"
print(names)
print(name1)'''