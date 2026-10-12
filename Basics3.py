'''
#Python Data Structures
#Lists 1
students = ["A", "S", "M"]
print(students[0])
print(students[1:3])

#List with append 
num = [18,5,23]
num.append(17)
print(num)

#List with insert 
num = [18,5,23]
num.insert(1,17)
print(num)

#List with remove
num = [18,5,23,17]
num.remove(17)
print(num)

#List with pop
num = [18,17,5,23]
num.pop(1)
print(num)

#List with sort(ascending order)
num = [18,5,23]
num.sort()
print(num)

#List with sort(Descending order)
num = [18,5,23]
num.sort()
num.reverse()
print(num)

#List with reverse
num = [18,5,23]
num.reverse()
print(num)
'''
'''
#Sets
#set creation
num={1,2,1,3,2,3}
print(num)

#set duplicates removing 
num=[1,2,1,3,2,3]
unique =list(set(num))
print(unique)

#set Checking Membership
num={10,20,30,40}
print(20 in num)
print(50 in num)

#set union
A={1,2,3}
B={3,4,5}
print(A|B)

#set intersection 
A={1,2,3}
B={3,4,5}
print(A.intersection(B))

#set difference
A={1,2,3}
B={3,4,5}
print(A-B)
'''