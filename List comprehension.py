areas1 = [ i*i for i in range(1,11) ]
areas2 = [ i*i for i in range(1,11) if i % 2 == 0]
areas3 = [ ( x, y ) for x in range(15) for y in range(15) ]

#print(areas1)
#print(areas2)
#print(areas3)

list1 = [8*a for a in range(1,13)]


print("list1 : ", list1)