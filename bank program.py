from distutils.command.build_ext import extension_name_re


# class College:
#        def __init__(self,ename,esal,eno):
#            self.ename = ename
#            self. sal = esal
#            self.eno =eno
#        def employee(self):
#            print("employee name:",self.ename)
#            print("employee name:",self.esal)
#            print("employee name:",self.eno)
# class staff:
#        def modifiy_name(clg):
#            clg.esal = clg.esal + 1000
#            College.employee()
# e=College("sruthi",5000,4)
# staff.modifiy_name(e)

# class Employee:
#     class Employee:
#         def __init__(self, name, emp_id, salary):
#             self.name = name
#             self.emp_id = emp_id
#             self.salary = salary
#
#     def display(self):
#         print("Employee Number:", self.name)
#         print("Employee Name:", self.emp_id)
#         print("Employee Salary:", self.salary)
#
# class Test:
#     def modify_sal(emp):
#         emp.esal = emp.esal + 5000
#         emp.display()
#
#
# # e = Employee("Ajay", 1001, 25000)
# # Test.modify_sal(e)

# class Employee:
#     def __init__(self, name, emp_id, salary):
#         self.name = name
#         self.emp_id = emp_id
#         self.salary = salary
#
#     def display(self):
#         print("Employee Number:", self.emp_id)
#         print("Employee Name:", self.name)
#         print("Employee Salary:", self.salary)
#
# class Test:
#     @staticmethod
#     def modify_sal(emp):
#         emp.salary = emp.salary +5000
#         emp.display()
#
# # Creating an Employee instance
# e = Employee("Ajay", 1001, 25000)
#
# # Modifying salary and displaying details
# Test.modify_sal(e)



class College:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def display(self):
        print("Employee Number:", self.emp_id)
        print("Employee Name:", self.name)
        print("Employee Salary:", self.salary)

class Test:
    @staticmethod
    def modify_sal(col):
        col.salary = col.salary +9000
        col.display()

# Creating an Employee instance
e = College("sruthi", 1001, 25000)

# Modifying salary and displaying details
Test.modify_sal(e)
