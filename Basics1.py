'''
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
'''
#Find largest of 3 numbers
