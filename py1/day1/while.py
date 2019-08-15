'''count = 0
while True:
    print("count",count)
    count = count +1
'''
#猜字游戏
age = 56
count = 0
while  count <3:
#for i in range(3):
    guss_age = int(input("age："))
    if age == guss_age:
         print("猜对了！")
         break
    elif  guss_age > age:
          print("大了")
    else:
          print("小了")
    count=count+1
    if count == 3:
        countine_confirm = input("do you want go on ?")
        if countine_confirm != "n":
            count =0
#这里的else是如果代码正常走完就走这里，如果是异常结束break了就不走这里了
else:
    print("猜太多次了")
