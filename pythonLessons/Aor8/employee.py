class Employee:
    """ Class variables """
    increase = 1.04


    def __init__(self,first_name, last_name, salary):
      self.first_name = first_name
      self.last_name = last_name
      self.salary = salary

    def __str__(self):
      return f'{self.first_name}, {self.last_name}, earns {self.salary}'
    
    def increase_salary(self):
      self.salary = int(self.salary * self.increase)
      
  
class Developer(Employee):
    increase = 1.10
    def __init__(self, first_name, last_name, salary, prog_lang):
       super().__init__(first_name, last_name, salary)
       self.prog_lang = prog_lang

    def __str__(self):
      return f'{super().__str__()} and fav prog lang is {self.prog_lang}'

emp1 = Employee('John', 'Doe', 50000)
emp2 = Employee('Jane', 'Doe', 60000)
emp3 = Developer('John', 'Doe', 50000, 'Python')

print(emp1)
print(emp2)
print(emp3)

emp1.increase_salary()
emp2.increase_salary()
emp3.increase_salary()
print(emp1)
print(emp2)
print(emp3)