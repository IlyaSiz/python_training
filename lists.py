from geom2d import *

l1 = [Point(0, 0), Point(1, 2), Point(2, 1)]
l2 = [Point(0, 0), Point(1, 2), Point(2, 1)]
l3 = l1
l4 = list(l1)

print(l1 == l2)
print(l1 == l3)
print(l1 == l4)

#списки равны, если ссылки на объекты совпадают
l4[0] = Point(0, 0)
print(l1 == l4)

l2 = sorted(l1)
print('ok') 
