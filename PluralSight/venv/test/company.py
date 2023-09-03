from employee import Employee, SalaryEmployee, HourlyEmployee, ComissionEmployee

class Company:
    def __init__(self):
        self.employees = []
        
    def add_employee(self, new_employee):
        self.employees.append(new_employee)
        
    def display_employees(self):
        print('Current Employees:')
        for i in self.employees:
            print(i.fname, i.lname)
        print('------------')
        
    def pay_employees(self):
        print('Paychecks:')
        for i in self.employees:
            print('Paycheck for:', i.fname, i.lname)
            print(f'Paycheck amount: ${i.calculate_paycheck():,.2f}')
        print('------------')
        
def main():
    my_company = Company()
    employee1 = SalaryEmployee("Sara", "Hess", 50000)
    my_company.add_employee(employee1)
    employee2 = HourlyEmployee("John", "Hess", 25, 50)
    my_company.add_employee(employee2)
    employee3 = ComissionEmployee("Roberto", "Perez", 40000, 5, 150)
    my_company.add_employee(employee3)
    
    my_company.display_employees()
    my_company.pay_employees()
main()