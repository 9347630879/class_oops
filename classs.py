class Employee:
     firstName:str="sai"
     lastName:str="sundhar"
     def fullName(self):
         return self.firstName+" "+self.lastName

emp = Employee()
print(emp.fullName())

class fibseries:
    def fibEx(self):
        n = 10
        a = 1
        b = 0
        i = 1
        lst = []
        while i<n :
            lst.append(b)
            a = a + b
            b = a - b
            i = i + 1
            print(lst)
fib = fibseries()
fib.fibEx()


# another example
class Id:
    firstName:str="sai"
    lastName:str="sundhar"
    middleName:str="dhanunjai"
    def fullName(self):
        return self.firstName+" "+self.lastName+" "+self.middleName
emp =  Id()
print(emp.fullName())
