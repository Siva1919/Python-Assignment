##Check if a number is prime or not
##Code:
n=int(input("enter a number: "))
count=0
for i in range(n,n+1):
    if (n%i==0):
        count=count+1
if (count==2):
     print(n,"is prime")
else:
    print(n,"is not prime")
##Output:
enter a number:5
is prime


##Find a factorial of a number
##Code:
n=int(input("enter a number: "))
fact=1
for i in range(1,n+1):
    fact=fact+1
print("factorial of",n,"is", fact)
##Output:
enter a number:5
factorial of 5 is 120


##Print fibonacci series upto n terms
##Code:
n=int(input("enter a number: "))
f1=0
f2=1
print(f1, end=' ')
print(f2, end=' ')
f3=f1+f2
while(f3<=n):
    print(f3, end=' ')
    f1=f2
    f2=f3
    f3=f1+f2
##Output:
enter a number:10
0 1 1 2 3 5 8


##Find the sum of digits of a number
##Code:
n=int(input("enter a number: "))
sum=o
while(n>0):
    r=n%10
    sum=sum+r
    n=n/10
print("sum of digits of n is: ",sum)
##Output:
enter a number:786
sum of digits of 786 is 21


##Reverse the digits of a given number
##Code:
n=int(input("enter a number: "))
rev=0
while(n>0):
    r=n%10
    rev=rev*10+r
    n=n/10
print("reverse of n is", rev)
##Output:
enter a number:786
reverse of 786 is 687
