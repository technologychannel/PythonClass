country_capital = {
    'Nepal': 'Kathmandu',
    'US': 'WDC',
    'Japan': 'Tokyo',
    'India': 'New Delhi',
    'Bangaladesh': 'Dhaka'
}


all_keys = list(country_capital.keys())
all_keys.sort()
all_keys.reverse()

for k in all_keys:
    print(f"Capital city of {k} is {country_capital[k]}")


## List and Dictonary are mostly used.

# print(f"Capital city of Nepal is {country_capital['Nepal']}")
# print(f"Capital city of US is {country_capital['US']}")
# print(f"Capital city of Japan is {country_capital['Japan']}")