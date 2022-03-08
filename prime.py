n1=int(input("enter the starting number:"))
n2=int(input("enter the ending number:"))
print("the prime numbers from",n1,"to",n2,"are")
for i in range(n1,n2):
    if(i%2!=0):
        print(i)
        
