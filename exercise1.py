##Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument
##def fact(n):
##    a=1
##    if(n>0):
##        for i in range(1,n+1):
##            a=a*i
##        return a
##    elif(n==1 or n==0):
##            return 1
##    else:
##        return -1
##print("the factorial of n is:",fact(-2))
##e.g:n=-2
##a=1
##if(-2>0):false
##elif(-2==1 or -2==0):false
##else
##the factorial of n is 1

##Write a Python function that takes a list and returns a new list with unique elements of the first list
##def uni(lists):
##    return list(set(lists))
##lists=[1,2,2,4,3]
##print("the unique element of lists:",uni(lists))

##def uni([1,2,2,4,3]):
##    return list(set([1,2,2,4,3])
##     return list({1,2,3,4})
##     return [1,2,3,4]
##    the unique element of lists :[1,2,3,4]
##Write a Python function to check whether a number is perfect or not
##def modulus(n):
##    a=0
##    for i in range(1,n):
##       if(n%i==0):
##           a=a+i
##    return a
##n=4
##modulus(n)
##if(n==modulus(n)):
##    print("{}is the perfect number".format(n))
##else:
##    print("{} is not a perfect number".format(n))
##def modulus(4):
##for i in range(1,4):
##    if(4%1==0):
##        a=0+1=1
##i=2
##if(4%2==0)
##a=1+2=3
##i=3
##if(4%3==0)
##return 3
##n=4
##modulus(4)=3
##if(4==3):false
## 4 is not a perfect number
##Write a Python function to create and print a list where the values are square of numbers between 1 and 30 (both included)
##def squares(n):
##    lists=[]
##    for i in range(1,n+1):
##         i=i*i
##         lists.append(i)
##    return lists
##print("the perfect  square number is ",squares(30))



##Write a Python function that checks whether a passed string is palindrome or not
##def palindrome(n):
##    s=""
##    for i in n:
##        s=i+s
##    return s
##n=input("enter the string")
##palindrome(n)
##if(n==palindrome(n)):
##    print("{} is a palindrome".format(n))
##else:
##    print("{} is not a palindrome".format(n))


##n=mom
##def palindrome(mom):
##    for i in mom:i=m
##       s=m+""=m
##    for i in mom:i=o
##    s=o+m=om
##     for i in mom:i=m
##    s=m+om=mom
##if(mom==mom):true
##mom is a palindrome




    
##Write a Python function to check whether a string is a pangram or not
def ispangram(s):
    n="abcdefghijklmnopqrstuvwxyz"
    for i in n:
        if i not in s:
           return False
    return True
s=input("enter the string:")
if(ispangram(s)==True):
    print("yes, is a pangram")
else:
    print("not an pangram")
    

        



