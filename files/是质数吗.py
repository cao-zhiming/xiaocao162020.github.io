num = int(input("请输入一个数字: "))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "不是质数")
            print(i, "乘于", num // i, "是", num)
            break
    else:
        print(num, "是质数")

else:
    print(num, "不是质数")