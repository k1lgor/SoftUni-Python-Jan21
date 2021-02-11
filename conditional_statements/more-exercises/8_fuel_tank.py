fuel = input()
liter = float(input())

if fuel == 'Gas' or fuel == 'Gasoline' or fuel == 'Diesel':
    if liter >= 25:
        print(f'You have enough {fuel.lower()}.')
    else:
        print(f'Fill your tank with {fuel.lower()}!')
else:
    print('Invalid fuel!')
