#printing my name 10 times
for i in range(10):
    print("Varshitha")

#Calculate sum of first N numbers
N=int(input("N="))
sum=0
i=1
while i<=N:
    sum=sum+i
    i=i+1
print(sum)

#Check if a number is even or odd
x= int(input("Number=")) 
if x%2==0:
    print( x ,"is a even number")
else:
     print( x ,"is a odd number") 

#printing multiplication table using for loop
x=int(input("Number="))
for i in range(1,11,+1): 
    print(x,"*",i,"=",x*i)
    i=i+1

#printing multiplication table using while loop
x=int(input("Number="))
i=1
while i<=10:
    print(x,"*",i,"=",x*i)
    i=i+1

# Check if a number is prime
x = int(input("Number="))
if x <= 1:
    print(x, "is not prime")
else:
    for i in range(2, x):
        if x % i == 0:
            print(x, "is not prime")
            break
    else:
        print(x, "is prime")

#Print FizzBuzz (print 1-100, multiples of 3→Fizz, 5→Buzz, 15→FizzBuzz)
for i in range(0,101,+1):
    print(i)
    if i%15==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")   
    else:
        print("number") 

#Find largest of 3 numbers
x= 18
y= 23
z= 5
if x>y and x>z:
    print(x,"is largest among 3 numbers")
elif y>x and y>z:
    print(y,"is largest among 3 numbers")
else:
    print(z,"largest among 3 numbers") 

#count digits in a number
x= int(input("enter the number"))
count=0
while x!=0:
    x=x//10
    count+=1
    print(count)

#Reverse the number
x=int(input("enter the number:"))
reverse=0
while x!=0:
    a=x%10
    reverse=reverse*10+a
    x=x//10
print(reverse)

#fibonacci sequence for first N terms
N=int(input("enter the number:"))
a=0
b=1
while N!=0:
    print(a)
    c=a+b
    a=b
    b=c
    N=N-1