"""
+, -
*, /
//  = integer division
**  = exponentiation
%   = mod
"""

import math
print('Repeater operation with multiplication:', '10' * 5)
print('Common division:', 10 / 3)
print('Integer Division (int values return int type):', 10 // 3)
print('Integer Division (float value anywhere returns float type):', 10 // 3.12)
print('Exponentiation:', 4 ** 4)
print('Mod (division result):', 19 % 4)

print("Absolute of -7.253 is (to positive):", abs(-7.253))
print("4, power of 3 is:", pow(4, 3))


print("Square root of 64 is:", math.sqrt(64))
print("Ceil and floor of 3.14 respectively: {} | {}".format(
    math.ceil(3.14), math.floor(3.14)))
print("Value of pi {:.7f}".format(math.pi))
