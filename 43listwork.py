### Creating List
names = ['Anish', 'Binod', 'Ratna']

### Add Item to List
names.append("Mahesh")
names.append("Prakash")
names.append("Manish")
names.append("Manish")

### Remove last item from list
# names.pop()

## Find total number of occurences
total_manish = names.count("Manish")
### Clear All
## names.clear()

### Index
print(f"{names[1]} {names[2]}")

### Find Index by Value of First Item
print(names.index("Manish"))

print(total_manish)


names.sort()

for name in names:
    print(name)

# for i in range(0, len(names)):
#     print(names[i])

# i = 0
# while(i<len(names)):
#     print(names[i])
#     i+=1


# expenses = [1000, 2500, 410]

# print(type(names))
# print(type(expenses))

