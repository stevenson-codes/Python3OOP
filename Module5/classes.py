class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)


class Tester(Employee):
    def run_tests(self):
        print(f'Testing is started by {self.name}...')
        print('Tests are done.')

class Developer(Employee):
    def __init__(self, name, age, salary, framework):
        super().__init__(name, age, salary)
        self.framework = framework

    def increase_salary(self, percent, bonus=0):
        super().increase_salary(percent)
        self.salary += bonus

employee1 = Tester("Joseph", 28, 2000)
employee2 = Developer("Linda", 22, 4000, "Flask")

employee2.increase_salary(20, 30)
print(employee2.name, employee2.framework)

