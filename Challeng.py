class Account:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance

    def disposite(self,dip):
        self.balance=self.balance+dip
        print(f"You added {dip}.")

    def withdraw(self,x):
        if x<self.balance:
            self.balance=self.balance-x
            print(f'Your withdrawd amount is {x}.')
            print(f'Now, your current balance is {self.balance}')
        else:
            print("Sorry! Not enough funds.")

    def __str__(self):
        return f'Owner : {self.owner} \nBalance : {self.balance}'
p=Account('Pops',10)
p.disposite(50)
p.withdraw(9)
print(p)


