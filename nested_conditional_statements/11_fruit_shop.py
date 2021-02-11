fruit = input()
day = input()
qnty = float(input())

if fruit == 'banana':
    if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
        qnty *= 2.5
        print(f'{qnty:.2f}')
    elif day == 'Saturday' or day == 'Sunday':
        qnty *= 2.7
        print(f'{qnty:.2f}')
    else:
        print('error')
elif fruit == 'apple':
    if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
        qnty *= 1.2
        print(f'{qnty:.2f}')
    elif day == 'Saturday' or day == 'Sunday':
        qnty *= 1.25
        print(f'{qnty:.2f}')
    else:
        print('error')
elif fruit == 'orange':
    if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
        qnty *= 0.85
        print(f'{qnty:.2f}')
    elif day == 'Saturday' or day == 'Sunday':
        qnty *= 0.9
        print(f'{qnty:.2f}')
    else:
        print('error')
elif fruit == 'grapefruit':
    if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
        qnty *= 1.45
        print(f'{qnty:.2f}')
    elif day == 'Saturday' or day == 'Sunday':
        qnty *= 1.6
        print(f'{qnty:.2f}')
    else:
        print('error')
elif fruit == 'kiwi':
    if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
        qnty *= 2.7
        print(f'{qnty:.2f}')
    elif day == 'Saturday' or day == 'Sunday':
        qnty *= 3
        print(f'{qnty:.2f}')
    else:
        print('error')
elif fruit == 'pineapple':
    if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
        qnty *= 5.5
        print(f'{qnty:.2f}')
    elif day == 'Saturday' or day == 'Sunday':
        qnty *= 5.6
        print(f'{qnty:.2f}')
    else:
        print('error')
elif fruit == 'grapes':
    if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
        qnty *= 3.85
        print(f'{qnty:.2f}')
    elif day == 'Saturday' or day == 'Sunday':
        qnty *= 4.2
        print(f'{qnty:.2f}')
    else:
        print('error')
else:
    print('error')
