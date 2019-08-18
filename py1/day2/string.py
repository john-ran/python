name = "john is OMG a {sex},he is {year} yearold 1 "
print(name.capitalize())
print(name.count("a"))
print(name.center(50,"-"))
print(name.endswith("n"))#判断string以什么结尾
print(name.expandtabs(tabsize=5))#如果string中有\t的话tabsize会把\t换成tabsize个空格
print(name.find("n"))#打印n的位置
print(name.format(sex='man',year=33))#初始化
print(name.format_map({'sex':'man','year':33}))
print('1232fdafasdf!'.isalnum())#当string只有数字与字母时候，返回真，如果有特殊字符返回假
print('lol'.isalpha())#只有字母是返回真
print('123d'.isdigit())#整数返回真
print('alol1'.isidentifier())#判断是否是一个合法的变量名
print('adfasf'.islower())#判断是不是小写
print('Dfaf'.istitle())
print('dfaf'.isprintable())
print('dfaf'.isupper())
print('+'.join(['1','2','3','4']))#把列表内容变成变量，重要
print(name.ljust(50,'+'))
print(name.rjust(50,'+'))
print(name.lower())
print(name.upper())
print("\nAlexdafaf".lstrip())#去除左边的回车
print('Alexdafaf\n'.rsplit())
print('\n    afdadfq\n    '.strip())#去除两边的回车与空格
print("-")
lol = str.maketrans("abjoh",'12345')#把12345对应给abjoh，
print("john son".translate(lol))#然后赋给string
print("johnson".replace("j","J"))#把j改成J，如果只改第一个后面加,1
print("johnson".rfind('n'))#从左开始找到最后一个sting的位置
print("joh nson".split(' '))#把string按照空格写成一个列表
print('1+2+3+4'.split('+'))
print("joh nson".swapcase())
print("joh nson".title())
print("joh nson".replace('j','J'))