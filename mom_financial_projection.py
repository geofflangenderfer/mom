import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# monthly income
garage = 0
house = 80*365/12
vacancy = -.25 * (garage + house)
property_management =  -.5 * (garage + house)

# monthly expenses
tax = 432
insurance = 125
electric = 94.52 # avg. monthly utility bill for MI
water = 0
sewer = 0
garbage = 0 
gas = 0
lawn = 100*9/12
snow = 100*3/12
repairs = 100
mortgage = 762.15

# build dataframe
col1 =    ['Income', 'Income', 'Income', 'Income', 
           'Expenses', 'Expenses', 'Expenses', 'Expenses',
           'Expenses', 'Expenses', 'Expenses', 'Expenses',
           'Expenses', 'Expenses', 'Expenses']
           
col2 =     ['Garage', 'House', 'Vacancy', 'Property Management',
           'Tax', 'Insurance', 'Electric', 'Water', 
           'Sewer','Garbage', 'Gas', 'Lawn',
           'Snow', 'Repairs', 'Mortgage']
values = [garage, house, vacancy, property_management, tax, insurance, 
          electric, water, sewer, garbage, gas, lawn, snow, repairs, mortgage] 
#tuples = list(zip(*arrays))
#index = pd.MultiIndex.from_tuples(tuples)

data = pd.DataFrame([col1, col2, values]).T
data.columns = ['Type1', 'Type2', 'Values']
print(data)

data.to_csv('house.csv', index=False)
## monthly cash flow
#total_monthly_cashflow = total_monthly_income_current - total_monthly_expenses
#
## cash on cash ROI
#repairs_start = 5000
#total_investment = repairs
#
#roi_yr1 = 12*total_monthly_cashflow/ total_investment
#
## roi after sale 
#house_value_current = 300000
#repairs_start = 5000
#cap_exp = 40000
#rental_income_yr1 = total_monthly_cashflow*12
#rental_income_yr2 = (400*6*12) + 80*365*.75 - 12*total_monthly_expenses
#
#house_value_sold = 600000
#print(data)
#data.to_csv('house.csv')
##income.to_csv('income.csv')
##expenses.to_csv('expenses.csv')
#
##print(income)
##print(expenses)
##print(cash_flow)
##print(cash_roi)
#
##dic = {'Income':{'Garage':garage, 'House':house},
##       'Expenses':{'Tax':tax, 'Insurance':insurance, 'Electric':electric,
##                   'Water':water, 'Sewer':sewer, 'Garbage':garbage, 
##                   'Gas':gas, 'Lawn':lawn, 'Snow':snow, 'Vacancy':vacancy,
##                   'Repairs':repairs, 'Cap. Ex.':cap_ex, 
##                   'Property Management':property_management, 
##                   'Mortgage':mortgage},
##       'Cash Flow': total_monthly_cashflow,
##       'Cash ROI':roi}
##data = pd.DataFrame(dic)
