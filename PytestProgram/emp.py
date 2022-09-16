class Employee():
    def __init__(self,name , salary):
        self.name = name
        self.salary = salary

    def as_dict(self):
        return [{"Name": self.name, "salary": self.salary}]


class Company():
    def __init__(self, company_name):
        self.company_name = company_name
        self.employee_dict = {}


    def add_employee(self, employee):
        a = self.employee_dict.update({employee.name:employee})
        return self.employee_dict
        # employee = employee_dict.upd
    def display_employee(self):
        for emp_detail in self.employee_dict:
            emp_obj = self.employee_dict.get(emp_detail)
            print(emp_obj.as_dict())


e = Employee("sachin", 20)
c = Company("tata")
c.add_employee(e)
c.display_employee()