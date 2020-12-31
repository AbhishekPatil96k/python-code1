a=444
def display():
    global a
    a=777
    b=666
    print(a)
    print(b)
def fun2():
    global a
    a=555
    c=888
    print(c)
    print(a)
display()
fun2()
print(a)