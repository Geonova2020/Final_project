class Employee:
    def __init__(self, name, hourly_rate):
        self.name = name
        self.hourly_rate = hourly_rate

    def calculate_salary(self, hours_worked):
        regular_hours = min(hours_worked, 40)
        overtime_hours = max(0, hours_worked - 40)
        
        regular_pay = regular_hours * self.hourly_rate
        overtime_pay = overtime_hours * (self.hourly_rate * 1.5) # 1.5x for overtime

        gross_salary = regular_pay + overtime_pay
        return gross_salary

# Example Usage
employee1 = Employee("Alice Smith", 25.00)
hours_worked_alice = 45
salary_alice = employee1.calculate_salary(hours_worked_alice)
print(f"{employee1.name}'s gross salary: ${salary_alice:.2f}")

employee2 = Employee("Bob Johnson", 30.00)
hours_worked_bob = 35
salary_bob = employee2.calculate_salary(hours_worked_bob)
print(f"{employee2.name}'s gross salary: ${salary_bob:.2f}")
