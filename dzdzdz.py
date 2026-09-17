def f(x):
    return x**3 - x - 2
qwe = 1.0
asd = 2.0
zxc = 0.0001
while abs(asd-qwe)>zxc:
    zxc1=(qwe+asd)/2.0
    if f(qwe)*f(zxc1)<=0:
        asd=zxc1
    else:
        qwe=zxc1
ww = (qwe+asd)/2.0
print (f'корень',ww)