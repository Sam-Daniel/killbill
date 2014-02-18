from bills import Bill
from datetime import date, timedelta

class MonthlyExpense:
    def __init__(self, date):
        self.month = date.month
        self.start = date(date.year,date.month,1)
        self.end = date(date.year,date.month,31)
        self.bills = []
        self.value = 0
    def addBill(self, bill):
        self.bills += [bill]
        daysInMonth = 0
        billDays = timedelta(bill.end - bill.start).days
        if billDays == 0:
            billDays = 1
        billPerDay = bill.value/billDays
        if bill.end.month == self.month:
            if bill.start.month == self.month:
                daysInMonth = billDays
            else:
                daysInMonth = timedelta(bill.end - self.start).days
        else:
            daysInMonth = timedelta(self.end - bill.start).days
        self.value += (billPerDay*daysInMonth)

