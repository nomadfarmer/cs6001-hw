#!/usr/bin/env python3
"""
2018-06-28 -- Joby/Nomadfarmer
Problem set 1 for the edX 6.00.1x MIT intro to CS courseself.
This code will be given variables for a credit card loan by the testing
suite. It will calculate the remaining balance after 12 months of paying
the mininum paymentself.
Variables passed include: balance, annualInterestRate, and monthlyPaymentRate.
"""
#Variables for testing
balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04


#Actual code to paste starts here.
def payAMonth(startBalance, payment):
    """
    Takes the balance at the beginning of the month, subtracts the payment,
    and adds the monthly interest. Returns the new balance.
    The variables received from the grading suite will be treated as constants.
    """
    newBalance = startBalance - payment
    newBalance *= 1 + (annualInterestRate / 12)
    return newBalance

def payAYear(startBalance, monthlyPayment = -1):
    """
    Run through a year of payments. If given a monthly payment, use that.
    Otherwise, calculate the minimum payment each month and use that.
    """
    newBalance = startBalance

    for month in range(12):
        newBalance = payAMonth(newBalance, monthlyPayment if monthlyPayment > 0 else newBalance * monthlyPaymentRate)
    return newBalance

#Main code starts here
curBalance = payAYear(balance)
print("Remaining balance:", round(curBalance, 2))
