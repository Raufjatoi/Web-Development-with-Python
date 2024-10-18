# lets ask for the user the input rather than hardcoding the table 
table = int(input('enter table : '))

for i in range(10): # range helps in like nums to repeat over rather than using list 
    print(f'{table} x {i+1} = {table * (i+1)}')