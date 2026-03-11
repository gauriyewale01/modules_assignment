import math_utils

print(math_utils.add(5, 3))        
print(math_utils.subtract(10, 4))

from math_utils import square
print(square(6)) 

import string_utils
print(string_utils.capitalized_words("hello world"))
print(string_utils.reverse_string("Python"))
print(string_utils.word_count("This is a test string."))

import shop_package.discount as disc
print(disc.apply_discount(1000, 10))

from shop_package.billing import calculate_total
print(calculate_total([100, 200, 300]))

from shop_package.billing import apply_tax
print(apply_tax(500))

from shop_package.discount import flat_discount
print(flat_discount(200))