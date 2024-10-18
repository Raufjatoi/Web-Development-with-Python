people = [
    {'name': 'Ahsan', 'age': 19},
    {'name': 'Rauf', 'age': 20},
    {'name': 'Umar', 'age':19}
]

people.sort(key=lambda person: person['name']) # lamda is short function we use when we dont need a big func like here to sort 
print(people)