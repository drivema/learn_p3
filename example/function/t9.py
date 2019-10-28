#!/usr/bin/python3

# 可写函数说明
def changeme(mylist):
    "修改传入的列表"
    mylist.append([1, 2, 3, 4])
    mylist.append((1, 2, 3, 4))
    mylist.append({"1":(1, 2, 3, 4)})
    print("函数内取值: ", mylist)
    return


# 调用changeme函数
mylist = [10, 20, 30]
t3 = {10, 20, 30}
changeme(mylist)
print("函数外取值: ", mylist)

print(mylist[5]["1"][0])

t2=mylist[5]["1"]
print(t2[0])
print(t3)

for i in t3:
    print(i)