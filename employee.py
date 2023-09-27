"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, salary=0, contract_time=1, commision_value=0, contract_commision_quantity=1 ):
        self.name = name
        self.salary = salary
        self.contract_time = contract_time
        self.commision_value = commision_value
        self.contract_commision_quantity = contract_commision_quantity

    def get_pay(self):
        return (self.salary * self.contract_time) + (self.commision_value * self.contract_commision_quantity)
        pass

    def __str__(self):
        string = f"{self.name} works on a "

        if self.contract_time > 1:
            string += f"contract of {self.contract_time} hours at {self.salary}/hour"
        elif self.salary > 0:
            string += f"monthly salary of {self.salary}"

        if self.contract_commision_quantity > 1:
            string += f" and receives a commision for {self.contract_commision_quantity} contract(s) at {self.commision_value}/contract."
        elif self.commision_value > 0:
            string += f" and receives a bonus commision of {self.commision_value}."
        else:
            string += '.'

        string += f"  Their total pay is {self.get_pay()}."
        return string


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie',4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', 25,100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee',3000,commision_value=200, contract_commision_quantity=4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', 25, 150,220,3 )

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', 2000,commision_value=1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', 30, 120, 600)
