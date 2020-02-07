class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Developer(Employee):
    def __init__(self, id, name, skills):
        super().__init__(id, name)
        self.skills = skills

    def __repr__(self):
        return  repr((self.id, self.name, self.skills));

rajesh = Developer(100, 'Rajesh', 'Java')

print(rajesh)