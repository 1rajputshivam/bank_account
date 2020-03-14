password=int(input("enter the password: "))
if password==1234:
    class account():
        def __init__(self,name,balance):
            self.name=name
            self.balance=balance
        def amount(self,amnt):
            self.amnt=amnt
            if self.balance>0:
                self.balance+=amnt
        def withdraw(self,wdth):
            self.wdth=wdth
            if self.balance>0:
                self.balance-=wdth
        def viewbalance(self):
            print(self.name,self.balance)
        acount1=account("shivam",10000)
        while True:
            print("1:- ammount \n 2:- witdhdraw\n 3:- check balance\n")
            choose=int(input("enter the option"))
            if choose==1:
                amnt1=int(input("enter the amount: "))
                acount1.amount(amnt1)
            elif choose==2:
                amnt1=int(input("enter the amountto witdhdraw"))
                acount1.withdraw(amnt1)
            else:
                acount1.viewbalance()
                break
else:
    print("Soory, Invalid password try again")
    