x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x = float(input())
y = float(input())

b1 = (x == x1 or x == x2) and (y1 <= y <= y2)
b2 = (y == y1 or y == y2) and (x1 <= x <= x2)

if b1 or b2:
    print('Border')
else:
    print('Inside / Outside')
