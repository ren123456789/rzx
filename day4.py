# -*-coding:UTF-8-*-


def peven(q):
    if q==1 or q==2:
        return 1;
    else:
        return peven(q-1)+peven(q-2)

q=int(input("请输入月份"))
print(peven(q))

