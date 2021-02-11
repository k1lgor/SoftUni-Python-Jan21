budget = float(input())
season = input()
dest = ''
room = ''

if budget > 3000:
    room = 'Hotel'
    budget *= 0.9
    if season == 'Summer':
        dest = 'Alaska'
    else:
        dest = 'Morocco'
elif 1000 < budget <= 3000:
    room = 'Hut'
    if season == 'Summer':
        budget *= 0.8
        dest = 'Alaska'
    else:
        budget *= 0.6
        dest = 'Morocco'
else:
    room = 'Camp'
    if season == 'Summer':
        budget *= 0.65
        dest = 'Alaska'
    else:
        budget *= 0.45
        dest = 'Morocco'
print(f'{dest} - {room} - {budget:.2f}')
