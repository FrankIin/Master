#%%
import datetime

class Employee:
    bonus_amount = 1.05
    number_of_employees = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        # self.email = f'{first.lower()}.{last.lower()}@mycompany.nl'
        self.pay = pay
        Employee.number_of_employees += 1

    def __repr__(self):
        return f'Employee({self.first}, {self.last}, {self.pay})'

    def __str__(self):
        return f'{self.fullname()} - {self.email}'

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

    @property
    def fullname(self):
        return(f'{self.first} {self.last}')

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print(f'Deleted {self.first} {self.last}')
        self.first = None
        self.last = None

    def apply_bonus(self):
        self.pay = int(self.pay * self.bonus_amount)

    @property
    def email(self):
        return f'{self.first.lower()}{self.last.lower()}@mycompany.nl'

    @classmethod
    def set_bonus_amount(cls, amount):
        cls.bonus_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay, *_ = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

class Developer(Employee):
    bonus_amount = 1.50
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print(f'--> {emp.first} {emp.last}')


emp_1 = Employee('Franklin', 'Kreleger', 5000)
emp_2 = Employee('John', 'Doe', 10000)

emp_1.first = 'Freek'
print(emp_1.email)
print(emp_1.fullname)
emp_1.fullname = 'Franklin Kreleger'
print(emp_1.fullname)

del emp_1.fullname


# %%
print(repr(emp_1))
print(emp_1.__repr__())

int.__add__(1,2)


print(len(emp_1))


dev_1 = Developer('test', 'test', 6000, 'python')
dev_2 = Developer('john', 'deer', 7000, 'java')

mgr_1 = Manager('Karen', 'Komplainer', 900000, [dev_1])

print(mgr_1.email)
mgr_1.print_emp()
mgr_1.add_emp(dev_2)
mgr_1.print_emp()
print(dev_1.prog_lang)



emp_str1 = 'Franklin-Kreleger-5000-123-123-123-123-123-123'
emp_str2 = 'John-Doe-5000-100'

new_emp_1 = Employee.from_string(emp_str1)

# print(new_emp_1.email)

my_date = datetime.date(2026, 9, 10)

print(Employee.is_workday(my_date))

print(Employee.number_of_employees)
print(Employee.number_of_employees)

Employee.set_bonus_amount(1.10)

emp_1 = Employee('Franklin', 'Kreleger', 5000)
emp_2 = Employee('John', 'Doe', 10000)
print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())
print(Employee.fullname(emp_1)) # same is above

print(emp_1.pay)
emp_1.apply_bonus()
print(emp_1.pay)


# %%
Employee.bonus_amount = 1.05
emp_1.bonus_amount = 1.20
print(Employee.bonus_amount)
print(emp_1.bonus_amount)
print(emp_2.bonus_amount)

# %%
print(emp_1.__dict__)
print(Employee.__dict__)