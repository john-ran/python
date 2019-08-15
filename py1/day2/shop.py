import sys
goods = [[1,"MAC",10000],[2,"手机",3000],[3,"耳机",200],[4,"平板",5000]]
print("欢迎来到斗牛国际商城")
salary = int(input("请输入你本次计划购买商品的资金："))
b = []
a = []
for m in range(0,4):
    a.insert(m,goods[m][2])
min = min(a)
time = 0
while time < 3:
    if min > salary:
        print("不好意思，您本次计划购买商品的资金小于本商城价格最低的商品,",min,"本次购物结束。")
        sys.exit(1)
    print(goods[:])
    i = int(input("请输入你想购买的商品编号：")) - 1
    print(goods[i][1])
    j = goods[i][2]
    if j <= salary:
        salary = salary -j
        print("购买成功。")
        b.insert(i,goods[i])
        print("剩余资金为：",salary)
        goon = input("继续购买吗？")
        if goon == "yes":
            continue
        else:
            print("您所购买的商品如下",b[:],"剩余资金",salary)
            sys.exit("购买完成。")
        if salary < min:
            print(goods[i][1],"购买成功","但剩余资金不足无法继续购买了")
            print(b[:])
            sys.exit(1)
    else:
        print("资金不足以购买此商品,请选择其它商品.")
    time = time +1