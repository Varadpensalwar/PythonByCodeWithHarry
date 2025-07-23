# class Emplooye:
#     def __init__(self, name, salary, bonds):
#         self.name = name
#         self.salary= salary
#         self.bond = bonds
    
#     def get_info(self):
#         return f"A salary of {self.name} is {self.salary} with {self.bond} years of bond"
# e = Emplooye("Varad",1000000000000,3)
# print(e.get_info())


class Emplooye:
    def __init__(self, name, salary, bonds):
        self.name = name
        self.salary= salary
        self.bond = bonds
    
    def get_info(self):
        print(f"A salary of {self.name} is {self.salary} with {self.bond} years of bond")
e = Emplooye("Varad",1000000000000,3)
e.get_info()