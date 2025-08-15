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
    def increase_salary(self, percent, bonus=0):
        super().increase_salary(percent)
        self.salary += bonus
