"""
Project 6 Fluffleshuffle Payroll
Alissa
Fluffleshuffle Payroll Program reads in Employees from a file and displays their information including the calculated not pay.
"""
# Import statements

#Classes
""" Define classes here """
import pygame, math
class Employee:
    # Define a constructor function
    def __init__(self,num,name,address,hourlyWage,hoursWorked):
        # assign instance data to each property
        self.num = num
        self.name = name
        self.address = address
        self.hourlyWage = hourlyWage
        self.hoursWorked = hoursWorked
    def calcPay(self):
        
        FT_HOURS = 40
        FED_TAK_RATE = .20
        STATE_TAX_RATE = .075
        OT_RATE = 1.5
        overtimePay = 0
        grossPay = 0 
        
        if self.hoursWorked <= FT_HOURS: 
            grossPay = self.hourlyWage * self.hoursWorked
        
        if self.hoursWorked > FT_HOURS:
            grossPay = self.hourlyWage * FT_HOURS
            overtimePay = (self.hourlyWage * OT_RATE * (self.hoursWorked - FT_HOURS))
        # calculate the total gross pay including overtimePay
        grossPay += overtimePay

        netPay = grossPay - (grossPay * FED_TAX_RATE) - (grossPay *STATE_TAX_RATE)

        return netPay

# Variables

#Constant

#Functions

#Main Program
keaton + Employee(1, "Keaton", "111 Main", 7, 10)

print(keaton.calcPay())