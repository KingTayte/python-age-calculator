# This is a python program that gives your age during any year

'''
This program takes into account the following variables:
1. Year of Birth, depicted by year_of_birth variable.
2. Year in which you want to calculate your age, depicted by age_year variable
3. Your age at that time of year depicted by age_at_year
'''

year_of_birth = int(input("Which year were you born? (Example. 2000): "))
age_year = int(input("Enter the year which you wish to know you age for (For example, 2026): "))

age_at_year = age_year - year_of_birth

print(f"You will be {age_at_year} years old in the year {age_year}")



# Program by Tatenda Mapfumo