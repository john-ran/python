#if-else流程判断
'''_name = 'john'
_password = '123456'
name = input("name:")
password = input("password:")
if _name == name and _password == password:
    print("welcome {name} login".format(name=name))
else:
    print("name or password is wrong.")
#for循环
for i in range(1,10):
    if i < 5:
        print(i)
    else:
         break#结束循环，单从运行结果上看不出区别，Debug选中代码一步一步可以看出
 #        continue#跳出本次循环，继续下次循环
    print("你好")
'''
for i in range(10):
    print("------",i)
    for j in range(10):
        print(j)
        if j > 5:
            break#跳出了j的循环





