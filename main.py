import sys # TODO now import only the function that is being used from module
import time

start = time.time()

set = range(100000)
print(f' The length of set is {len(set)} numbers')

list = list(set)
tuple = tuple(set)
# TODO: call list and tuple funcs several times

print(type(list))
print(type(tuple))

print(f'Size of list is {sys.getsizeof(list)} bytes')
print(f'Size of tuple is {sys.getsizeof(tuple)} bytes')
# TODO reformat code to fit only 89 positions per line
print(f'The difference in memory between tuple and list is {sys.getsizeof(list)-sys.getsizeof(tuple)} bytes')

end = time.time()
print(f'Runtime is {end-start} sec')
if __name__ == '__main__':
    main()
