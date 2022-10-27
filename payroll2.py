# They now have 3 classifications of employees:
# 1. Hourly
# 2. Salaried
# 3. Commissioned

# Employee classes have the following required attributes:
# emp_id: string
# first_name: string
# last_name: string
# address: string
# city: string
# state: string
# zipcode: string
# classification: a concrete instance of either Hourly, Salaried, or Commissioned

class Employee:
    def __init__(self, emp_id, first_name, last_name, address, city, state, zipcode, classification):
        self.emp_id = emp_id
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.classification = classification

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.emp_id})"

    def __repr__(self):
        return f"{self.first_name} {self.last_name} ({self.emp_id})"


# abstract classification
class Classification:
    def __init__(self, hourly_rate, salary, commission_rate):
        self.hourly_rate = hourly_rate
        self.salary = salary
        self.commission_rate = commission_rate

    def __str__(self):
        return f"{self.hourly_rate} {self.salary} {self.commission_rate}"

    def __repr__(self):
        return f"{self.hourly_rate} {self.salary} {self.commission_rate}"


# Hourly classification
class Hourly(Classification):
    def __init__(self, hourly_rate):
        super().__init__(hourly_rate, None, None)
        self.hourly_rate = hourly_rate

    def __str__(self):
        return f"Hourly: ${self.hourly_rate}"

    def __repr__(self):
        return f"Hourly: ${self.hourly_rate}"


# Salaried classification
class Salaried(Classification):
    def __init__(self, salary):
        super().__init__(None, salary, None)
        self.salary = salary

    def __str__(self):
        return f"Salaried: ${self.salary}"

    def __repr__(self):
        return f"Salaried: ${self.salary}"


# Commissioned classification
class Commissioned(Classification):
    def __init__(self, commission_rate):
        super().__init__(None, None, commission_rate)
        self.commission_rate = commission_rate

    def __str__(self):
        return f"Commissioned: ${self.commission_rate}"

    def __repr__(self):
        return f"Commissioned: ${self.commission_rate}"


# PayrollSystem class
# There are 24 pay periods per year. Twice each month, 1/24th of a salary is paid to employees
# who receive a salary. Do not include taxes and other deductions.
# Commissioned employees are salaried employees, but also receive an additional payment of their total
# sales times their commission rate.
# Hourly employees are simply paid their hourly rate times their hours worked for that pay period. We will not include overtime.
# Employees can have their classifications changed during their employment.
class PayrollSystem:
    def __init__(self, employees):
        self.employees = employees

    def __str__(self):
        return f"{self.employees}"

    def __repr__(self):
        return f"{self.employees}"

    def calculate_payroll(self):
        for employee in self.employees:
            if employee.classification.salary:
                print(
                    f"{employee.first_name} {employee.last_name} ({employee.emp_id}): ${employee.classification.salary / 24}")
            elif employee.classification.commission_rate:
                print(
                    f"{employee.first_name} {employee.last_name} ({employee.emp_id}): ${employee.classification.commission_rate / 24}")
            elif employee.classification.hourly_rate:
                print(
                    f"{employee.first_name} {employee.last_name} ({employee.emp_id}): ${employee.classification.hourly_rate}")
            else:
                print(f"{employee.first_name} {employee.last_name} ({employee.emp_id}): ${0}")

    def change_classification(self, emp_id, new_classification):
        for employee in self.employees:
            if employee.emp_id == emp_id:
                employee.classification = new_classification
                print(
                    f"{employee.first_name} {employee.last_name} ({employee.emp_id}) classification changed to {employee.classification}")