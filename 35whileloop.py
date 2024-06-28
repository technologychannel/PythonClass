atm_pin = '1456'
user_pin = ''
attempt = 0

while atm_pin != user_pin:
    user_pin = input("Enter ATM Pin: ")
    if attempt>0:
        print(f"Invaid pin code. Total Attempt {attempt}")
    attempt = attempt + 1


print("Access Granted. How much you want to withdraw?")    