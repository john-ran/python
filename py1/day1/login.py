import os,sys,getpass
i = 0
j = 0
m = 0
while i < 3:
    name = input("请输入你的用户名：")
    lockfile = open('lock.txt', 'r')
    locklist = lockfile.readlines()
    for lockname in locklist:
        lname = lockname.strip('\n')
        if lname == name:
            sys.exit("你已经被锁定了，快来找我解锁吧。")
    userinfo = open('user.txt', 'r')
    for line in userinfo.readlines():
        user, password = line.strip('\n').split()
        if user == name:
            while j < 3:
                ypassword = input("请输入你的密码：")
                if password == ypassword:
                    sys.exit("登陆成功！")
                else:
                    print("密码输入错误，请重新输入：")
                    j = j + 1
                    if j == 3:
                        sys.exit("密码输入错误超过三次，结束本次登陆。")
    if name != lname and name != user:
        #while m < 3:
            m = m + 1
            print("用户名输入错误，请重新输入。")
            #m = m + 1
            if m == 3:
                print("\033[0;31m%s\033[0m"%"用户名输入错误超过三次，退出本次登陆。")
                break