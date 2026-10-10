'''
#functions
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

#lambda with sorted
students = [
    ("Varshitha",22),
    ("Smriti",18),
    ("Jemi",5)
]
x= sorted(students,key=lambda student:student[1])
print(x)

#lambda with sorted string
Team = [
    ("Smriti",18),
    ("Jemi",5),
    ("Harman",7)
]
x= sorted(Team,key=lambda team:team[0])
print(x)
'''

#lambda with descending order sorted 
Team = [
    ("Smriti",18),
    ("Jemi",5),
    ("Harman",7)
]
x= sorted(Team,key=lambda team:team[0],reverse=True)
y= sorted(Team,key=lambda team:team[1],reverse=True)
print(x)
print(y)
 