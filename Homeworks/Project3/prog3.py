import functools #includes built in reduce function
L = [-1.2, 3.3333, -5.6, 5.0, 3.0001, 2.5, 2.8]

#Problem 5
itr = map(lambda x : 0.0 if x < 0.0 else x, L)
print('Negative numbers removed: ', list(itr))


#Problem 6
print('Minimum in the list: ', functools.reduce(lambda x, y : x if x < y else y, L))


#Problem 7
Fitr = filter(lambda x : x >= 2.0 and x <= 3.0, L)
print('Values where 2.0 <= x <= 3.0: ', list(Fitr))
