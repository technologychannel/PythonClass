names = [
    # name, department
    ("Sagar Aryal", "Microbiology"),
    ("Santosh Adhikari", "IT"),
    ("Subin Thapa", "IT"),
    ("Mandip Hirachan", "IT"),
    ("Sujan Khadka", "Finance"),
    ("Samyak Pokharel", "MBA"),
    ("Binod Rayamajhee", "Microbiology")
]

### Fina All From Microbiology Department
microbiology_names = [name for name in names if name[1] == "Microbiology"]

for i in microbiology_names:
    print(i[0])


### Create 10 employee who works on different department
### Print all employee who are in IT Department

### Option: 
### Display all department along with their names.