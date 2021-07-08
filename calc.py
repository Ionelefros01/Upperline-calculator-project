# Budget and Vacation calculator (Stress)

# Data inputs:

budget = input("What is your net monthly salary? ")
essential_spendings = input("How much money do you spend on living expenses? ")
# save_account = input("How much money do you want to send to the saving account? ")
vacation_expenses = input("How much money does your vacation requires? ")
stress_level = input("On a scale of 1 to 10 how stressfull you felt this year? ") 


# Calculate the saved money:

money_saved = (int(budget) - int(essential_spendings)) * 12

print(f"\nFor the past year you saved ${money_saved}!")

save_account = input("How much money do you want to send to the saving account? ")


money_you_can_spend = ((int(budget) - int(essential_spendings))  * 12 - int(save_account))

# Function for stress level

def vacation_stress_status(number):
    if number <= str("6") :
        return ("You may not need a vacation." + "\n" + "\n" + "However, if you want one there is some information about your financial status:")
    elif number > str("6"): 
        return ("You definetly need a vacation!" "\n" + "\n" + "There is some information about your financial status:")

print("\n" + vacation_stress_status(stress_level))

print(f"\nFor the past year you saved ${money_saved}!")

print(f"\nBecause you want to send ${save_account} to your saving account, you can spend just ${money_you_can_spend}")

def enough_money_for_vacation(money):
    if int(money_you_can_spend) >= int(vacation_expenses):
        return (f"Your vacation cost ${vacation_expenses}, so you can afford it. Have a great vacation!")
    if int(money_you_can_spend) < int(vacation_expenses):
        return (f"Your vacation cost ${vacation_expenses}, so you can't afford it. Please save more money and try to go on a vacation next year.")

print ("\n" + enough_money_for_vacation(vacation_expenses) + "\n")


    
   

