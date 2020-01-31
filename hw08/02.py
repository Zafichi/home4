class Department:
    def __init__(self, name, employees, budget):
        self.name = name
        self.employees = employees
        self.budget = budget

    class BudgetError(ValueError):
        pass

    def get_employees(self):
        return ', '.join(self.employees.keys())

    def get_budget_plan(self):
        try:
            budget_of_department = float(self.budget - sum(self.employees.values()))
            if budget_of_department < 0:
                raise self.BudgetError
        except ValueError:
            print('Budget is negative!')
        return float(self.budget - sum(self.employees.values()))

    def get_average_salary(self):
        return round(float(sum(self.employees.values()) / len(self.employees.values())), 2)

    def __add__(self, other):
        return (
            f'{self.name} - {other.name}',
            {**self.employees, **other.employees},
            self.budget + other.budget
        )

    def merge_departments(self, *args):
        for i in args:
            self.name += ' - ' + i.name
            self.employees.update(i.employees)
            self.budget += i.budget
        self.get_budget_plan()
        return self

    def __str__(self):
        dep = f'{self.name} ({self.get_employees()} - {self.get_average_salary()}, {self.budget})'
        return dep

    def __or__(self, other):
        return self.name if self.get_budget_plan() >= other.get_budget_plan() else other.name


department_1 = Department('Football', {'Alex': 1200, 'Pavel': 2500, 'Inna': 1800}, 12000)
department_2 = Department('Hokey', {'Max': 3100, 'Nikolas': 2200, 'Frodo': 2300}, 12000)
department_3 = Department('Tennis', {'Patric': 2400, 'Spirit': 1200, 'Linda': 3300}, 15100)
new_department = department_1 + department_2
print(new_department)
print(department_1.merge_departments(department_2, department_3))
print(department_1 | department_2)

