#!/usr/bin/env python3
"""
2018-06-28 -- Joby/Nomadfarmer
Problem set 2 for the edX 6.00.1x MIT intro to CS courseself.
This code will be given variables for a credit card loan by the testing
suite.

Variables passed include: balance, annualInterestRate.

This time, the goal is to find the lowest fixed payment (same payment each month)
which will pay off the debt within one year.

"""
#Variables for testing
balance = 3926
annualInterestRate = 0.2

def main():
    curBalance = balance
    #payments must be multiples of 10. We're starting our search at $10. I'd start
    #at the minimum monthly payment, but the specs on this problem don't mention a
    #minimum monthly payment rate.

    fixedPayment = 0
    while curBalance > 0:
        fixedPayment += 10
        curBalance = payAYear(balance, fixedPayment)

    print("Lowest Payment:", fixedPayment)


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

main()
