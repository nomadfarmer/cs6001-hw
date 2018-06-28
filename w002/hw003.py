#!/usr/bin/env python3
"""
2018-06-28 -- Joby/Nomadfarmer
Problem set 3 for the edX 6.00.1x MIT intro to CS courseself.
This code will be given variables for a credit card loan by the testing
suite.

Variables passed include: balance, annualInterestRate.

This time, the goal is to find the lowest fixed payment (same payment each month)
which will pay off the debt within one year.

"""
#Variables for testing
balance = 320000
annualInterestRate = 0.2

#Actual code to paste starts here.

def main():
    epsilon = 0.25 #most we're willing to overpay in a year. It's hard to tell
                   #what a reasonable value is. Too picky, and we risk finding
                   #an infinite loop. 25 cents seems to work for me, but I don't
                   #even know how to test for edge cases.
    curBalance = balance
    upperLimit = balance * (1 + annualInterestRate)
    lowerLimit = balance / 12

    while curBalance < -epsilon or curBalance > 0:
        fixedPayment = round((upperLimit + lowerLimit) / 2, 2) # In the real world, we can't pay partial cents.
        curBalance = payAYear(balance, fixedPayment)
        if curBalance > 0:
            lowerLimit = fixedPayment
        elif curBalance < -epsilon:
            upperLimit = fixedPayment

    print("Lowest Payment:", fixedPayment)


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
