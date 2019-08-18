#元组
'''names = ('lpl','omg')
print(names.count('lpl'))
a = []
a.insert(1,1)
print(a)'''
list = [
    ("app",50,1),
    ["orange",3,0],
    ("MAC",998,2)
]
while True:
    for b,item in enumerate(list):
        print(b,item)
    break
print(list[:])