class Emplooye :
    company = "asus"
    def __init__(self, name , salary, bond,company):
        self.name = name
        self.salary = salary
        self.bond = bond
        self.company = company

    def get_info(self):
        return f"A salary of {self.name} is {self.salary} with {self.bond} years of bond in {self.company}"

e = Emplooye("varad",1000,5,"BMW")
print(e.get_info()) 
print(Emplooye.company)
print(e.company)
print(dir(e))