n=int(input("Enter first no. :"))
m=int(input("enter second no. :"))
l=[]
k=[]
p=[]
for i in range(1,n+1):
    if n%i==0:
        l=l+[i]
for j in range(1,m+1):
    if m%j==0:
        k=k+[j]
p=p+k
for i in l:
    if i  not in k:
        p=p+[i]
    else:
        pass
        
print(p[-1])
