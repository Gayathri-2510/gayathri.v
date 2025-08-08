a=int(input("Enter a integer: "))
odd=[]
for i in range(a):
    c=str(2 * i + 1)
    odd.append(c)
print(", ".join(odd))
