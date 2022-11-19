class Employee:

    raise_amt = 1.05

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
    
    @property
    def email(self):
        return  '{}{}@email.com'.format(self.first,self.last)
    
    @property
    def full_name(self):
        return '{} {}'.format(self.first,self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

# first_name = input("Enter the first name : ")
# last__name = input("Enter the last name : ")
# pay = int(input("Enter your salary : "))

# Services = Employee(first_name,last__name,pay)
# print(f"\n\nABOUT :\nName : {Services.full_name}\nEmail : {Services.email}\nPay : {Services.pay}")

