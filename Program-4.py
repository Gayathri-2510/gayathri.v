list1=[1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
count={}
for i in range(1, 10):
    c=0
    for j in list1:
        if j%i==0:
            c+=1
    count[i]=c
print(count)
