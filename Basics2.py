'''
class Student:
    def study(self, name, age):
        print(name ,"is the Student of age", age)

    def write_exam(self, name):
        print(name,"is the fan of Smriti")
s1=Student()
s1.study("varshitha", 18)
print(s1.study)
s1.write_exam("Varshitha")

#lambda function with 1 arugument
def fun(x):
    fun=lambda x:x*x
    print(fun(x))
fun(5)

#lambda function with multiple variables
def cal(a,b):
    add=lambda a,b: a+b
    mul=lambda a,b: a*b
    print(add(a,b))
    print(mul(a,b))
cal(18,5)

#lambda function using if/else
def check(x):
    check=lambda x: "EVEN" if x%2==0 else "ODD"
    print(check(x))
check(18) 
'''   
