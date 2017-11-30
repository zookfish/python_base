

class SchoolMember:
    '''代表任何学校里的成员'''
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def tell(self):
        print('{} is {}'.format(self.name,self.age),end= ' ')


class Techer(SchoolMember):
    '''代表老师'''
    def __init__(self,name,age,salary):
        SchoolMember.__init__(self,name,age)
        self.salary = salary

    def tell(self):
        SchoolMember.tell(self)
        print('Salary:{:d}'.format(self.salary))


class Stucent(SchoolMember):
    '''代表学生'''
    def __init__(self,name,age,marks):
        SchoolMember.__init__(self,name,age)
        self.marks = marks


    def tell(self):
        SchoolMember.tell(self)
        print('Marks is {:d}'.format(self.marks))


t = Techer('Mr Peng',26,10000)
s = Stucent('yunux',26,150)

Mems = [t,s]
for mem in Mems:
    mem.tell()



