# count é um iterador sem fim (itertools)



from itertools import count

c1= count(16, 8)
r1 = range(16, 100, 8)

print('c1:', hasattr(c1, '__next__'))  # True
print('r1:', hasattr(r1, '__next__'))  # False
print('c1:', hasattr(c1, '__iter__'))  # True
print('r1:', hasattr(r1, '__iter__'))  # True

print('count')
for i in c1:
    if i > 100:
        break
    else:
        print(i)

print()

print('range')
for i in r1:
    print(i)