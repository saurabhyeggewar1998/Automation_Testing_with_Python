from emp import Company, Employee


class TestEmployeeWage:
    def test_add_contact(self):
        emp = Company("fisdom")
        employee_dict = {"name": "saurabh", "salary": 21}
        contact = Employee(**employee_dict)
        assert len(emp.employee_dict) == 0
        emp.add_employee(contact)
        assert len(emp.employee_dict) == 1
