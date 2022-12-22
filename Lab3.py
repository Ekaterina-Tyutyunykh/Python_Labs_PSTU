
from pyDatalog import pyDatalog

sum_of_numbers = ((0 + 999999) * 1000000) / 2  # сумма ряда считается по парам

average_of_numbers = sum_of_numbers / 1000000

median_of_numbers = 100 / 2  # так как диапазон 1-100

pyDatalog.create_terms('Sum_of_numbers, Average_of_numbers,Median_of_numbers,Prod_series_of_numbers_sqrt')

pyDatalog.create_terms('Factorial, N')
Factorial[N] = N * Factorial[N - 1] # произведене 1-100 = 100!
Factorial[1] = 1

print((Sum_of_numbers==sum_of_numbers)&(Average_of_numbers==Sum_of_numbers/1000000)&(Median_of_numbers==median_of_numbers)&(Prod_series_of_numbers_sqrt==Factorial[100]))
