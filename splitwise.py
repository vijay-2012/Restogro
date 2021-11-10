from collections import defaultdict
class splitWise:

    persons = []
    itr = 0
    transaction = {}

    total=defaultdict(lambda:0)
    def __init__(self):

        pass

    class person:

        def __init__(self, name):
            self.name = name
            pass

    class expenses:

        def __init__(self, payer, amount, recipients, share):
            self.payer = payer
            self.amount = amount
            self.recipients = recipients
            self.share = share

            pass
    class expenses_paid:

        def __init__(self, payer, amount):
            self.payer = payer
            self.amount = amount
            
            pass
    def addPerson(self, name):
        p = self.person(name)
        self.persons.append(p.name)


    def showPersons(self):
        for name in self.persons:
            print(name)

    def addExpense(self, payer, amount, recipients, share):
        self.itr += 1
        expense = self.expenses( payer, amount, recipients, share)
        split_amounts = []
        for i in expense.share:
            split_amounts.append(expense.amount * (i/100)) 
        self.transaction[self.itr] = {'payerName': expense.payer, 'amount': expense.amount, 'recipients':expense.recipients, 'share_amount': split_amounts }
    def total_expenses(self):
        for i in self.transaction.keys():
            for j in range(len(self.transaction[i]['recipients'])):
                self.total[self.transaction[i]['recipients'][j]] +=self.transaction[i]['share_amount'][j] 
    def expense_paid(self,payer,amount):
        self.total[payer]-=amount
    def show_debt(self):
        print(dict(self.total))
    def showExpense(self):
        print(self.transaction)



    



    

s = splitWise()
s.addPerson('vijay')
s.addPerson('Vig')
s.showPersons()
s.addExpense('Vijay', 50, ['Vig', 'Key'], [25,25])
s.addExpense('Vig', 100, ['Vijay', 'Key'], [50,50])
s.showExpense()
s.total_expenses()
s.expense_paid('Key',62.5)
s.show_debt()

