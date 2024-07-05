numbers = [1,2,3,4,5,6]

x = 2

even_numbers = [num for num in numbers if num%2==0]

print(type(even_numbers))

names = ['Anish', 'Binod', 'Ratna', 'Suman', 'Aryan', 'Bibek']

start_with_a = [name for name in names if name[0].lower() == 'a']
print(start_with_a)


### Find all names start with A

# even_numbers= []

# for num in numbers:
#     if num % 2 == 0:
#         even_numbers.append(num)

# print(even_numbers)