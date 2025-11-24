#Create a class called PersonAccount. It has firstname, lastname, incomes, expenses properties and it has total_income, total_expense, account_info, add_income, add_expense and account_balance methods. Incomes is a set of incomes and its description. The same goes for expenses.

class PersonAccount:
    def __init__(self,firstname='keshar',lastname='shrestha'):
        self.firstname=firstname
        self.lastname=lastname
        self.incomes={}
        self.expenses={}

    def add_income(self,description,num):
        self.incomes[description]=num
    
    def add_expense(self,description,num):
        self.expenses[description]=num

    def total_income(self):
        total=0
        for amount in self.incomes.values():
            total+=amount
        return amount
    
    def total_expense(self):
        total=0
        for amount in self.expenses.values():
            total+=amount
        return amount

    def account_balance(self):
        balance=self.total_income()-self.total_expense()
        return balance

    # --- Account Information ---
    def account_info(self):
        info = f"Account Holder: {self.firstname} {self.lastname}\n"
        info += "\n--- Incomes ---\n"
        for desc, amt in self.incomes.items():
            info += f"{desc}: {amt}\n"

        info += "\n--- Expenses ---\n"
        for desc, amt in self.expenses.items():
            info += f"{desc}: {amt}\n"

        info += f"\nTotal Income: {self.total_income()}\n"
        info += f"Total Expense: {self.total_expense()}\n"
        info += f"Account Balance: {self.account_balance()}\n"
        return info

person = PersonAccount()

person.add_income("Salary", 5000)
person.add_income("Part-time", 1200)

person.add_expense("Rent", 1500)
person.add_expense("Food", 500)

print(person.account_info())
