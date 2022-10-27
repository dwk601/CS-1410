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
from abc import ABC, abstractmethod
import os, os.path, shutil

PAY_LOGFILE = 'paylog.txt'

EMPLOYEES_FILE = 'employees.csv'
TIMECARDS_FILE = 'timecards.csv'
RECEIPTS_FILE = 'receipts.csv'

employees = []

def load_employees():
    '''
    Reads "employees.csv, creates Employee objects and puts them in the list named employees.
    '''
    employee_file = open(EMPLOYEES_FILE)
    for line in employee_file:
        employee_data = line.split(",")
        employee_object = Employee(employee_data[0], employee_data[1], employee_data[2], employee_data[3], employee_data[4], employee_data[5], employee_data[6], employee_data[7])
        employees.append(employee_object)
        if employee_data[7] == "3":
            employee_object.make_hourly(employee_data[10])
        elif employee_data[7] == "2":
            employee_object.make_commissioned(employee_data[8], employee_data[9])
        else:
            employee_object.make_salaried(employee_data[8])

def find_employee_by_id(emp_id_num):
    '''
    Searches the list of employees, finds the matching ID and returns the employee object.
    '''
    for emp in employees:
        if emp.emp_id == emp_id_num:
            return emp

def process_timecards():
    '''
    Reads the file "timecard.csv and add the hours to the corresponding employee.
    '''
    timecard_file = open(TIMECARDS_FILE)
    for line in timecard_file:
        emp_hrs = line.split(",")
        for emp in employees:
            if emp.emp_id == emp_hrs[0]:
                for hr in emp_hrs[1:]:
                    hr = float(hr)
                    emp.classification.timecards.append(hr)

def process_receipts():
    '''
    Reads the file "receipts.csv and adds the sales to the corresponding employee.
    '''
    receipt_file = open(RECEIPTS_FILE)
    for line in receipt_file:
        emp_sales = line.split(",")
        for emp in employees:
            if emp.emp_id == emp_sales[0]:
                for sale in emp_sales[1:]:
                    sale = float(sale)
                    emp.classification.sales.append(sale)

def run_payroll():
    '''
    Removes the old paylog.txt and creates new one to write out to.
    '''
    if os.path.exists(PAY_LOGFILE):
        os.remove(PAY_LOGFILE)
    for emp in employees:
        emp.issue_payment()


class Employee():
    '''
    This class contains the Employee attributes: emp_id, first_name, last_name, address, city, state, zipcode, classification.
    '''

    def __init__(self, emp_id, first_name, last_name, address, city, state, zipcode, classification):
        self.emp_id = emp_id
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.classification = classification

    def make_hourly(self, hourly_rate):
        '''
        Classificies the employee as an hourly employee.
        '''
        self.classification = Hourly(hourly_rate)

    def make_commissioned(self, salary, commission_percentage):
        '''
        Classifies the employee as a commissioned employee.
        '''
        self.classification = Commissioned(salary, commission_percentage)

    def make_salaried(self, salary):
        '''
        Classifies the employee as a salaried employee.
        '''
        self.classification = Salaried(salary)

    def issue_payment(self):
        '''
        Writes payment amount out to the file along with employee information.
        '''
        paylog_file = open(PAY_LOGFILE, "a")
        payAmount = self.classification.compute_pay()
        paylog_file.write(f"Mailing {payAmount} to {self.first_name} {self.last_name} at {self.address} {self.city} {self.state} {self.zipcode}\n")


class Classification(ABC):
    '''
    An abstract base class for the three different types of employees: Hourly, Commissioned and Salaried.
    '''

    @abstractmethod
    def compute_pay(self):
        return 0

class Hourly(Classification):
    '''
    The Hourly employee class computes the payment for hourly employees.
    '''

    def __init__(self, hourly_rate):
        self.hourly_rate = hourly_rate
        self.timecards = []

    def compute_pay(self):
        '''
        Computes payment for employee
        '''
        total_pay = sum(self.timecards) * float(self.hourly_rate)
        return round(total_pay, 2)

    def add_timecard(self, hours):
        '''
        Adds hours to an employee
        '''
        self.timecards.append(hours)

class Salaried(Classification):
    '''
    The Salaried employee class returns the salary for Salaried employees.
    '''

    def __init__(self, salary):
        self.salary = salary
        
    def compute_pay(self):
        '''
        Returns the salary
        '''
        return self.salary

class Commissioned(Salaried):
    '''
    The Commissioned employee class returns the salary plus commissions for employee.
    '''

    def __init__(self, salary, commission_percentage):
        self.salary = salary
        self.commission_percentage = commission_percentage
        self.sales = []

    def compute_pay(self):
        '''
        Computes the payment for Commissioned employees.
        '''
        com_percent = float(self.commission_percentage) * 0.01
        total_sales = sum(self.sales)
        total_pay = float(self.salary) + (total_sales * com_percent)
        return round(total_pay, 2)

    def add_receipt(self, amount):
        '''
        Adds receipt to a Commissioned employee.
        '''
        self.sales.append(amount)
