number1 = input("Enter Number 1: ")
number2 = input("Enter Number 2: ")



sum = int(number1) + int(number2)

print(f"Total is {sum}")


### Create a program, that convert Nepali Currency to USD, Euro, Japnease
### Enter Amount in NRS: 5000
### USD is: $45
### Euro is: $43
### Japnease amount is: 8454

# Create a Python program that converts Nepali currency to USD, Euro, and Japanese Yen;
# for example, if you enter the amount in NRS as 5000, it should display the converted
# amounts as USD $45, Euro €43, and Japanese ¥8454.

# Input from the user
r = float(input("Input Nepali Currency in Nepali Rupees: "))

# Source from Google as per 6/22/2024
a1_euro = 142.56
a2_usd = 133.35
a3_yen = 0.83

# Calculations
b1 = r / a1_euro
b2 = r / a2_usd
b3 = r / a3_yen

# Printing the results
print(f"Nepali Rupee in Euro is: €{b1:.2f}")
print(f"Nepali currency in USD is: ${b2:.2f}")
print(f"Nepali currency in Japanese Yen is: ¥{b3:.2f}")
