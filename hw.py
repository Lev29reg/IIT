import math
a = int(input())
b = int(input())
c = int(input())
if (b**2) - (4*a*c) >= 0:
    x1 = ((-1*b) + math.sqrt((b**2) - (4*a*c))) / (2 * a)
    x2 = ((-1*b) - math.sqrt((b**2) - (4*a*c))) / (2 * a)
    print (x1, x2)
else:
    print ('Loser')