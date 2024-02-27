"""Compares the filling speed of dynamic and
   immutable arrays.
"""


import time

element_count = 10_000_000
start_time = time.time()
data_1 = [None] * element_count
for data_index in range(element_count):
    data_1[data_index] = f'Some new value {data_index}'
print(
    'Creating a list with 10 million empty elements and populating it',
    time.time() - start_time
)


start_time = time.time()

data_2 = []

for data_index in range(element_count):
    data_2.append(f'some new value {data_index}')
print(
    'Creating empty list and adding 10 million items to it:',
    time.time() - start_time
)
