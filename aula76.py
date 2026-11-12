# copy - retorna uma cópia rasa (shallow copy)

import copy

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [1, 2, 3],
}

d2 = copy.copy(d1)  # shallow copy
d2 = copy.deepcopy(d1)  # deep copy

d2['c1'] = 1000
d2['l1'][1] = 999999

print(d1)
print(d2)