def avg(a,b,c):
    d = (a+b+c)/3
    return f"{d:.2f}"

value = avg(56,6,6)
print(value)


def keywordd(a,b,defaultt=4):
    x=a+b+defaultt
    return x

value = keywordd(46,6,8)
print(value)

value1= keywordd(b=4,a=3, defaultt=345)
print(value1)
    