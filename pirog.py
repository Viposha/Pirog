import sys
import time

start = time.time()
set = range(100000)
print(f' The length of set is {len(set)} numbers')

list = list(set)
tuple = tuple(set)

print(type(list))
print(type(tuple))

print(f'Size of list is {sys.getsizeof(list)} bytes')
print(f'Size of tuple is {sys.getsizeof(tuple)} bytes')
print(f'The difference in memory between tuple and list is {sys.getsizeof(list)-sys.getsizeof(tuple)} bytes')

end = time.time()
print(f'Runtime is {end-start} sec')