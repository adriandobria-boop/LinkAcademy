class Employee:
    
    def __init__(self, name, salary):
    
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"{self.name} are {self.salary} salariu Euro"
    
    def __int__(self):
        return self.salary
    
    def display(self):
        return f"{self.name} are {self.salary} salariu Euro"

    def anual_salary(self):
        return self.salary * 12
    
    def increase_salary(self, percent = 10):
        if percent in range(1, 101):
            self.salary += self.salary + percent / 100
        return self.salary
    
    def __iadd__(self, percent):
        if percent in range(1, 101):
            self.salary += self.salary + percent / 100
        return self
    
    def compare_salary(self, other_employee:Employee):
        return self.salary > other_employee.salary
    
    def __gt__(self, other):
        return self.salary > other.salary
    
angajat1 = Employee ("florin", 1000)
print(angajat1)
print(angajat1.display())
print(angajat1.name)

angajat2 = Employee ("Ioana", 1200)
print(angajat2)
print(angajat2.display())
print(angajat2.name)

rezultatul_transformarii_in_str = str(angajat2)
print(rezultatul_transformarii_in_str)

rezultatul_transformarii_in_int = int(angajat2)
print(rezultatul_transformarii_in_int)

print(angajat2.anual_salary())

angajat2.increase_salary(50)
print(angajat2)

print(angajat2.compare_salary(angajat1))
print(angajat2 > angajat1)

print(angajat1.compare_salary(angajat2))
print(angajat1 > angajat2) # __gt__


print(angajat2)
angajat2 += 10 # __iadd__
print(angajat2)






