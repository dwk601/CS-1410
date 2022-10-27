# #Requirements
# # Implement your design From Part 13, including the five module-level functions called in test_payroll.py by the due date. Use test_payroll.py as-is for your main module. Don’t change it. Run it as a normal Python program, not as a pytest or unittest module.
# After running your tests, compare the three new entries in paylog.txt to paylog_old.txt that was copied earlier in main, and verify that the pay amount has been changed appropriately for the three employees updated in main. Submit your payroll.py, paylog_old.txt, and paylog.txt output files.

# After you have run the tests in the file test_payroll.py, payroll.txt should contain:
# Mailing 5599.44 to Issie Scholard at 11 Texas Court Columbia Missouri 65218
# Mailing 2584.64 to Reynard Lorenzin at 3233 Spaight Point Houston Texas 77030
# Mailing 1880.00 to Jed Netti at 85 Coolidge Terrace San Antonio Texas 78255


# Here is a suggested development sequence:
#1.Write load_employees. It opens employees.csv, ignores the first line, and then reads a line at a
#   time, splitting its arguments on a comma. Create a new Employee object initialized with the string
#   attributes. Then create the appropriate instances for the employee’s classification and add it as an
#   attribute to the new Employee object. Finally, add the Employee object to your global list of employees.
#2.Write find_employee_by_id by searching the list of employees and returning the Employee object.
#3.Implement Employee
#4.Implement the Classification Hierarchy
#5.Implement process_timecards
#6.Implement process_receipts
import os

PAY_LOGFILE = 'paylog.txt'
EMPLOYEES_FILE = 'employees.csv'
TIMECARDS_FILE = 'timecards.csv'
RECEIPTS_FILE = 'receipts.csv'

employees = []

class Employee:
    def __init__(self, id, name, address, type):
        self.id = id
        self.name = name
        self.address = address
        self.type = type
        self.classification = None

    def make_salaried(self, salary):
        self.classification = SalariedClassification(salary)

    def make_hourly(self, hourly_rate):
        self.classification = HourlyClassification(hourly_rate)

    def make_commissioned(self, salary, commission_rate):
        self.classification = CommissionedClassification(salary, commission_rate)

    def issue_payment(self):
        amount = self.classification.calculate_pay()
        self.pay(amount)

    def pay(self, amount):
        with open(PAY_LOGFILE, 'a') as f:
            f.write(f'Mailing {amount} to {self.name} at {self.address}')
            
            
class Classification:
    def __init__(self):
        self.timecards = []
        self.receipts = []

    def add_timecard(self, hours):
        self.timecards.append(hours)

    def add_receipt(self, amount):
        self.receipts.append(amount)

    def calculate_pay(self):
        raise NotImplementedError('Subclass must implement abstract method')
    
class SalariedClassification(Classification):
    def __init__(self, salary):
        super().__init__()
        self.salary = salary

    def calculate_pay(self):
        return self.salary / 24
    
class HourlyClassification(Classification):
    def __init__(self, hourly_rate):
        super().__init__()
        self.hourly_rate = hourly_rate

    def calculate_pay(self):
        total_hours = sum(self.timecards)
        if total_hours > 8:
            overtime = total_hours - 8
            total_hours = 8 + overtime * 1.5
        return total_hours * self.hourly_rate
    
class CommissionedClassification(Classification):
    def __init__(self, salary, commission_rate):
        super().__init__()
        self.salary = salary
        self.commission_rate = commission_rate

    def calculate_pay(self):
        total = self.salary / 24
        total += sum(self.receipts) * self.commission_rate / 100
        return total
    
def load_employees():
    with open(EMPLOYEES_FILE) as f:
        next(f)
        for line in f:
            id, name, address, type = line.strip().split(',')
            employee = Employee(id, name, address, type)
            if type == 'Salaried':
                employee.make_salaried(3000)
            elif type == 'Hourly':
                employee.make_hourly(15)
            elif type == 'Commissioned':
                employee.make_commissioned(2500, 10)
            employees.append(employee)
            
def find_employee_by_id(id):
    for employee in employees:
        if employee.id == id:
            return employee
        
def process_timecards():
    with open(TIMECARDS_FILE) as f:
        next(f)
        for line in f:
            id, hours = line.strip().split(',')
            employee = find_employee_by_id(id)
            employee.classification.add_timecard(float(hours))
            
def process_receipts():
    with open(RECEIPTS_FILE) as f:
        next(f)
        for line in f:
            id, amount = line.strip().split(',')
            employee = find_employee_by_id(id)
            employee.classification.add_receipt(float(amount))
            
def issue_payments():
    for employee in employees:
        employee.issue_payment()
        
def main():
    if os.path.exists(PAY_LOGFILE):
        os.remove(PAY_LOGFILE)
    load_employees()
    process_timecards()
    process_receipts()
    issue_payments()

if __name__ == '__main__':
    main()
