# Create function that find square of number
import math

## Square root finder
sq_root = math.sqrt(25)

### 
number = 3.15454444
print(f"Number is {number:.2f}")

n1 = math.ceil(10.1)
n2 = math.floor(10.3)
print(n1)
print(n2)

n3 = math.pow(2,3)
print(n3)

print(round(10.6))

### 10.30
### 10.60

### Create function that round number 
### Enter number: 3.11
### Round is: 3

def round_number(n):
    round_num = round(n)
    print(f"Round number is {round_num} ")


user_input = float(input("Enter number: "))
round_number(user_input)