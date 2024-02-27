num=input("enter the num:").split(" ")
for i in range(len(num)-1):
    for j in range(i+1,len(num)):
        if(int(num[i]))<(int(num[j])):
            number=num[i]
            num[i]=num[j]
            num[j]=number
print("Descending Order:",f"{num}")
