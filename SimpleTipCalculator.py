# Import Statements

# Constants
EXE_TIP_RATE = .20
AVG_TIP_RATE = .15
POR_TIP_RATE = .10


# Variables
meal_cost = 0


# Functions

# define a function that calculates the tip amount 
# given the meal_cost and tip_rate
def tip_amount(meal_cost,tip_rate):
    #return the meal_cost * tip_rate
    return meal_cost * tip_rate


# define a function that calculates the total_cost
# given the meal_cost ant Tip amount
def total_cost(meal_cost,tip_amount):
    #return the meal_cost + tip_amount
    return meal_cost + tip_amount

# Main Function or Program

# Prompt the user for the meal cost
meal_cost = float(input("Enter the cost of the meal: $"))

# Print out the second line showing the meal cost
print("Cost of meal: ${:,.2f}".format(meal_cost))

exe_tip_amount = tip_amount(meal_cost,EXE_TIP_RATE)
exe_total_cost = total_cost(meal_cost,exe_tip_amount)
# Print out the third line showing the Tip amount and total meal cost
print("Excellent Service tip: ${:,.2f}".format(exe_tip_amount))
print("total: ${:,.2f}".format(exe_total_cost))

avg_tip_amount = tip_amount(meal_cost,AVG_TIP_RATE)
avg_total_cost = total_cost(meal_cost,avg_tip_amount)
# Print out the fourth line showing the Average Service tip
print("Average Service tip: ${:,.2f}".format(avg_tip_amount))
print("total: ${:,.2f}".format(avg_total_cost))

por_tip_amount = tip_amount(meal_cost,POR_TIP_RATE)
por_total_cost = total_cost(meal_cost,por_tip_amount)
# Print out the fifth line showing the Poor Service tip
print("Poor Service tip: ${:,.2f}".format(por_tip_amount))
print("total: ${:,.2f}".format(por_total_cost))