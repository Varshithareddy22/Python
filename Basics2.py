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
'''

#lambda function
def fun(x):
    fun=lambda x:x*x
    print(fun(x))
fun(5)