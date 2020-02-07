class Employee:

    def __init__(self, name='default'):
        self.name = name
        print('Constructor')

rajesh_employee = Employee('Rajesh Kannan')
default_employee = Employee()

print(default_employee.name)
print(rajesh_employee.name)
