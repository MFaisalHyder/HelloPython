"""
Slicing on strings with wrong indexes doesn't give index out of bound error
"""

String1 = "Tutorial"
string2 = "Faisal"

# Concatenation
print("concatenation + =>", String1 + " " + string2)

# Index
print("index | Tutorial[2] =>", String1[2])
print("index | Tutorial[-3] =>", String1[-3])  # starts reading from the end of String
# print(String1[9])  # index out of bound error
# print(String1[-9])  # index out of bound error

# Slicing ~ substring
print("slicing | Tutorial =>", String1[3:6])
print("slicing | Faisal =>", string2[3:5])  # right limit is not included
print("slicing | Faisal =>", string2[9:10])  # index [no index out of bound error in case of slicing]

# Multiple
print("multiple * =>", String1 * 4)

# Type Specific Functions
print("find() => ", String1.find("al"))  # -ve value represents means param not found in String, else index is returned
print("replace() =>", String1.replace("Tu", "New"))  # if found then it will be replaced else no change will occur
print("split() =>", String1.split("t"))
print("count() =>", String1.count("t", 3, 5))  # search param, starting index, ending index
print("upper() =>", String1.upper())  # turns string into upper case
print("lower() =>", String1.lower())  # turns string into lower case

# max() [returns alphabet i.e. in highest order, in case of mixed case, lower case is taken into account]
print("max() =>", max('mnAYacPrvZ'))
# min() [returns alphabet i.e. in lowest order, in case of mixed case, upper case is taken into account]
print("min() =>", min('wDpGXeCZYacA'))

print("isalpha() =>", String1.isalpha())  # checks if given string comprises of only characters or not.
print("isnumeric() =>", String1.isnumeric())  # checks if given string comprises of only numbers or not.
