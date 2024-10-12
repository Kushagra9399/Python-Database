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
        while True:
            print("Enter Name: ")
            name = input()
            if len(name)<3:
                print("Invalid format!!!\nName should contain minimum of 3 characters...")
            else:
                break
        self.name = name
    def set_year(self):
        while True:
            print("Enter Year: ")
            while True:
                try:
                    year = int(input())
                    break
                except Exception:
                    print("Enter Integer: ")
            if len(year)!=4:
                print("Invalid format!!!\nEnter year of four digit...")
            else:
                break
        self.year = year
    def set_mob(self):
        while True:
            print("Enter Mobile Number: ")
            mob = input()
            if len(mob)!=10:
                print("Invalid format!!!\nMobile Number of 10 digits needed...")
            else:
                break
        self.mob = mob
    def set_email(self):
        while True:
            print("Enter Email: ")
            email = input()
            if email.endswith("@gmail.com")==False:
                print("Invalid format!!!\nEmail should ends with \"@gmail.com\"")
            else:
                break
        self.email = email
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
