print("\n EXPENSE FORECASTING MODEL ")

# January data
jan_expenses = {
    'Groceries': 399.78,
    'Eating out': 103.10,
    'Skincare & makeup': 24.95,
    'Miscellaneous': 404.37,
    'Gifts': 67.79,
    'Offering/Donations': 35.62,
    'Transportation': 195.93,
    'Going out Activities': 87.00,
    'Nini Signs': 63.43,
    'Rent': 1350.00,
    'Apple bill': 29.57,
    'Phone bill': 110.71,
    'Tithe/Offerings': 431.00,
    'Giving': 193.81
}

# February data
feb_expenses = {
    'Groceries': 508.69,
    'Eating out': 48.93,
    'Clothes': 76.79,
    'Skincare & makeup': 36.00,
    'Miscellaneous': 14.74,
    'Offering/Donations': 24.00,
    'Transportation': 180.78,
    'Wellness': 132.00,
    'Rent': 1350.00,
    'Apple': 29.57,
    'Phone bill': 75.00,
    'Tithe/Offerings': 431.00,
    'Giving': 250.00
}
jan_total = sum(jan_expenses.values()) #gets all the numbers (ignoring the category names) 
feb_total = sum(feb_expenses.values()) #gets all the numbers (ignoring the category names)

print("\n MONTHLY TOTALS:")
print("January: $",jan_total) #the comma lets you combine the text and numbers 
print("February: $",feb_total)

dollar_change = feb_total - jan_total
percent_change = (dollar_change/jan_total) * 100

print("\n CHANGE FROM JAN TO FEB")
print("dollar_change: $", dollar_change)
print("percent_change:", percent_change, "%")

print("\n MARCH PREDICTIONS")
march_predictions = feb_total + dollar_change
print("predicted March Spending: $", march_predictions)

print("\n CATEGORY ANALYSIS FOR FEBRUARY") 
all_categories = set(list(jan_expenses.keys()) + list(feb_expenses.keys())) 
#set removes duplicates
#list converts them all into a list
for category in all_categories:
    jan_amount = jan_expenses.get(category, 0)
    feb_amount = feb_expenses.get(category, 0)
#get(category, 0) means "get the amount for this category, or use 0 if it doesn't exist"
    if jan_amount > 0 or feb_amount > 0:
        cat_change = feb_amount - jan_amount 
        if cat_change > 0:
            print(category, ": Increased by $", cat_change)
        elif cat_change < 0:
            print(category, ": Decreased by $", abs(cat_change)) #abs means absolute value so -54.17 will return 54.17
        else:
            print(category, ": No change")



