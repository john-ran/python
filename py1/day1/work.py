#编写登陆接口
'''
1.输入用户名密码
2.登陆成功后显示欢迎
3。输错三次后锁定，下次无法登陆
'''
#三级菜单
'''
1.可以按照菜单输入跳转到下一级菜单
2.任何一级的菜单都可以退出程序并可以返回上一级
'''
'''import sys
print(sys.path)#d打印环境变量
print(sys.argv)#打印相对路径
import os
#dir = os.system("dir")#执行dir命令，不保存结果
mydir = os.popen("dir").read()
#os.mkdir("new_dir")#创建一个新目录
print(mydir)'''
