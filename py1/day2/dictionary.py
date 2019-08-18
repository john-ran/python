#字典的存在形式是key-values的形式
import sys
china = {
    "安徽":{
        "合肥":{
            1:["庐江区","常住人口5w"],
            2:["蜀山区","常住人口7w"],
            3:["政务区","常住人口10w"]
        },
        "淮南":{
            1:["寿县","常住人口5w"],
            2:["八公山区","常住人口15w"]
        }
    },
    "江苏":{
        "南京":{
            1:["雨花台","常住人口10w"],
            2:["玄武区","常住人口15w"],
            3:["秦淮区","常住人口20w"]
        },
        "无锡":{
            1:["江阴","常住人口10w"],
            2:["锡山","常住人口6w"],
            3:["宜兴","常住人口8w"]
        }
    },
    "浙江":{
        "杭州":{
            1:["滨江","常住人口18w"],
            2:["上城区","常住人口50w"],
            3:["下城区","常住人口80w"]
        },
        "宁波":{
            1:["江北","常住人口18w"],
            2:["余姚","常住人口18w"],
            3:["慈溪","常住人口18w"],
        },
    }
}
sheng = list(china.keys())
a = 0
j = 0
z = 0
time = 0
while time < 3:
    print(sheng)
    i = input("请输入你要查询的省份,或者q/quit退出本次查找:")
    if i == "江苏":
        print(list(china[i].keys()))
        city1 = input("请输入你要查找的城市：")
        if city1 == "南京":
            print(china[i][city1])
        elif city1 == "无锡":
            print(list(china[i][city1].values()))
    elif i == "安徽":
        while a < 3:
            print(list(china[i].keys()))
            city1 = input("请输入你要查找的城市：")
            if city1 == "合肥":
                print(list(china[i][city1].values()))
            elif city1 == "淮南":
                print(list(china[i][city1].values()))
            elif city1 != "合肥" and city1 != "淮南":
                a = a + 1
                print("您输入的城市有误，请重新输入")
                if a == 3:
                    print("\033[31m%s\033[0m"%"您输入错误城市的次数过多，结束本次查找。")
                    break
    elif i == "浙江":
        print(list(china[i].keys()))
        city1 = input("请输入你要查找的城市：")
        if city1 == "杭州":
            print(list(china[i][city1]))
    elif i == "q" or i == "quit":
        sys.exit(0)
    else:
        time = time + 1
        print("您输入的城市错误，或者不在本次查找的字典中。请重新输入：")
        if time == 3:
            print("\033[31m%s\033[0m"%"输入的错误次数太多了")
            break











'''
school = {
    "class1":{
        "stu1":["johnson","man",25],
        "stu2":["john","man",23]
    },
    "class2":{
        "stu1":["jack","man",33],
        "stu2":["jackson","man",23]
    },
    "class3":{
        "stu1":["tom","man",16],
        "stu2":["amy","girl",18]
    }
}
school["class3"]["stu2"][2]=16
print(school)
while True:
    for i in school:
        print(i)
    j = input("选择你要取得班级：")
    if j == 'class1':
        print(school[j])
    elif j == 'class2':
        print(school[j])
    elif j == 'class3':
        print(school[j])
    else:
        print("输入错误，请重新输入")

info = {
    'stu1':'johnson',
    'stu2':'jack',
    'stu3':'omg',
    'stu4':'john'
}#地点是无序的
print(info)
print(info.get("stu1"))
print('stu1' in  info)#判断是否有stu1
#print(info["stu1"])
info["stu1"] = "JOHNSON"
print(info['stu1'])
info['stu5'] = 'TOM'
del info['stu1']
info.pop('stu2')
info.popitem()#随机删除一个
print(info)
'''