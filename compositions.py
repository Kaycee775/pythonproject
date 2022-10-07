class employee:

    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary

    def check_salary(self):
        return self.salary.check_salary()

class salary:

    def __init__(self, amount, bonus):
        self.amount = amount
        self.bonus = bonus

    def check_salary(self):
        return f"Marketer's salary is {self.amount * self.bonus} with a bonus of {self.bonus}"

marketer_salary = salary(50000, 5)
marketer_employee = employee("Richard", "Marketing", marketer_salary) 

print(marketer_employee.check_salary())