a = eval(input('请输入第一个数：'))
b = eval(input('请输入第二个数：'))
if a > b:
    for i in range(b, 0, -1):
        if a % i == 0 and b % i == 0:
            print('最大公因数是{}'.format(i))
            break
elif b > a:
    for i in range(a, 0, -1):
        if a % i == 0 and b % i == 0:
            print('最大公因数是{}'.format(i))
            break
else:
    print('两数相等')


