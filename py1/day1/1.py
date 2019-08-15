#标准输出的三种方法
name = input("name:")
age = int (input("age:"))
sex = input("sex:")
info1 = '''
---------info of %s--------
name:%s
age:%d
sex:%s
''' % (name,name,age,sex)
print(info1)
info2 = '''
---------info2 of {name}--------
name:{name}
age:{age}
sex:{sex}
''' .format(name=name,
            age=age,
            sex=sex)
print(info2)
info3 = '''
---------info3 of {0}--------
name:{0}
age:{1}
sex:{2}
''' .format(name,age,sex)
print(info3)
import getpass ##密文
name = input("name:")
password = getpass.getpass("password")
print(name,password)