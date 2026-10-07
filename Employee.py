class Employee:
    def __init__(self, name, salary=500):
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        return self.salary


class Manager(Employee):
    def __init__(self, name, bonus):
        super().__init__(name, 500 + bonus)


class Developer(Employee):
    def __init__(self, name, hours, rate):
        super().__init__(name, hours * rate)


m = Manager("Ana", 200)
d = Developer("Carlos", 40, 15)

print(m.name, m.calculate_salary())
print(d.name, d.calculate_salary())
