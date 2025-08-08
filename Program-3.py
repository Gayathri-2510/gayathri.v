a=int(input("Enter a integer: "))
if a<=2:
    print("1")
else:
    odd=[]
    for i in range(a - 1):
        odd.append(str(2 * i + 1))
    print(", ".join(odd))
