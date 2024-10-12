class Student:
    count = 0
    def __init__(self):
        self.count += 1
        self.id = self.count
        self.set_name()
        self.set_year()
        self.set_mob()
        self.set_email()
    def set_name(self):
        print("Enter Name: ")
        self.name = input()
    def set_year(self):
        print("Enter Admission Year: ")
        self.year = input()
    def set_mob(self):
        print("Enter Mobile Number: ")
        self.mob = input()
    def set_email(self):
        print("Enter Email: ")
        self.email = input()
    def get_name(self):
        return self.name
    def get_year(self):
        return self.year
    def get_mob(self):
        return self.mob
    def get_email(self):
        return self.email
    def display(self):
        print("Serial Number: ",self.id)
        print("Name: ",self.name)
        print("Year: ",self.year)
        print("Mobile Number: ",self.mob)
        print("Email: ",self.email)