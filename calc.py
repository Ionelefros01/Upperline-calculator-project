# Budget and Vacation calculator (Stress)

# Data inputs:

budget = input("What is your net monthly salary? ")
essential_spendings = input("How much money do you spend on living expenses? ")
vacation_expenses = input("How much money does your vacation requires? ")
stress_level = input("On a scale of 1 to 10 how stressfull you felt this year? ") #Done

# Calculate the saved money:

money_saved = (int(budget) - int(essential_spendings)) * 12


# Function for stress level

def vacation_stress_status(number):
    if number <= str("6") :
        return "You may not need a vacation."
    elif number > str("6"): 
        return "You definetly need a vacation!"

print(vacation_stress_status(stress_level))

print(f"For the past year you saved ${money_saved}!")

def enough_money_for_vacation(money):
    if int(money_saved) >= int(vacation_expenses):
        return (f"You vacation cost ${vacation_expenses} so you can afford it")
    if int(money_saved) < int(vacation_expenses):
        return (f"You vacation cost ${vacation_expenses} so you can't afford it. Please save more money and try to go on a vacation next year.")

print (enough_money_for_vacation(vacation_expenses))


    
   

