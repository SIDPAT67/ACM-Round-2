
class Employee:

    num_of_emps = 0
    raise_amt = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower() + '.' + last.lower() + '@comapany.com'

        Employee.num_of_emps += 1

    def fullname(self):    
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)    


class Developer(Employee):
    raise_amt = 1.1

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay) 
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)    

    def print_emps(self):
        for emp in self.employees:
            print("-->", emp.fullname())



        
emp_1 = Employee('James', 'Bond', 50000)
emp_2 = Employee('Elon', 'Musk', 60000)
dev_1 = Developer('Mike', 'Tyson', 40000, 'Python')
dev_2 = Developer('Mark', 'Rober', 80000, 'Java')      
mgr_1 = Manager('Bill', 'GAtes', 90000, [dev_1,emp_1])

#print(dev_1.email)
#print(dev_1.pay)
#print(dev_1.prog_lang)
print(mgr_1.email)

print()
mgr_1.print_emps()
print()
mgr_1.add_emp(dev_2)
mgr_1.print_emps()
print()
mgr_1.remove_emp(emp_1)
mgr_1.print_emps()

print(isinstance(mgr_1, Developer))
print(issubclass(Manager, Employee))
