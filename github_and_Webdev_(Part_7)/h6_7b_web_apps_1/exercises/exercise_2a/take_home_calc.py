# Get inputs from user, cast as integers and store in variables
monthly_take_home = int(input("What's your monthly take home income?"))
housing_costs = int(input("What's your monthly housing cost (rent/mortgage)?"))
food_costs = int(input("How much do you spend on food per month?"))
utility_costs = int(input("How much do you spend on utilities per month?"))

# Calculate remaining money after housing, food and utility costs
remaining = monthly_take_home - housing_costs - food_costs - utility_costs

# Calculate the percentage of take home that housing costs represent
housing_perc = housing_costs / monthly_take_home

# Print the message to the user
print (f"Your monthly amount after housing, food and utility costs is",
       f"£{remaining}.  Your housing costs represent {housing_perc*100:.2f}%",
       f"of your monthly take home.")
