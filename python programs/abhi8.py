l=[]
i=0
while(i<=4):
    print('enter the element')
    num=int(input())
    l.insert(i,num)
    i=i+1
k=list(filter(lambda num:num%2==0,l))
print(k)

