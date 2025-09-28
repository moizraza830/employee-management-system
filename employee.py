class Employee:
    def __init__(self, name, employee_id, base_salary):
        self.name= name
        self.employee_id= employee_id
        self.salary= base_salary

    def get_details(self):
        return f"Name: {self.name}, ID:{self.employee_id}, Salary: ${self.salary:,.2f}"
    
    def calculate_annual_bonus(self):
        return self.salary * 0.10
    
class Manager(Employee):
    def __init__(self, name, employee_id, base_salary, team_size):

        super().__init__(name, employee_id, base_salary)
        self.team_size=team_size

    def get_details(self):
        basic_details=super().get_details()
        return f"{basic_details}, Team Size: {self.team_size}"
    
    def calculate_annual_bonus(self):
        return (self.salary * 0.15) + (self.team_size * 500)
    
class Developer(Employee):
    def __init__(self, name, employee_id, base_salary, programming_language):
        super().__init__(name, employee_id, base_salary)
        self.language= programming_language

    def get_details(self):
        return f"{super().get_details()}, Language: {self.language} "
    
    def calculate_annual_bonus(self):
        return super().calculate_annual_bonus()
    

# Abstraction
class Company:
    def __init__(self, name):
        self.name=name
        self._employees= []

    def hire(self, employee):
        self._employees.append(employee)
        print(f"{employee.name} has been hired by {self.name}.")

    def display_roster(self):
        # Displays  details for all employees
        print("\n --- Employee roster for {self.name} ---")
        for emp in self._employees:
            print(emp.get_details())
        print("-" * 30)

    def calculate_total_bonus_payout(self):
        total_bonus= 0
        print("\n --- Calculate Annual Bounous ---")
        for emp in self._employees:
            bonus=emp.calculate_annual_bonus()
            print(f"Bonus for {emp.name}: ${bonus:,.2f}")
            total_bonus += bonus

        print("-" * 30)
        print(f"Total bonus payout for the company: ${total_bonus:,.2f}")

emp1=Manager("Alif", "008", 900000, 10)
emp2 = Developer("Bob Smith", "D001", 75000, "Python")
emp3 = Developer("Charlie Brown", "D002", 80000, "JavaScript")

my_company= Company("google")
my_company.hire(emp1)
my_company.hire(emp2)
my_company.hire(emp3)

my_company.display_roster()
my_company.calculate_total_bonus_payout()