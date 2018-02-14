"""
Tuple is a sequence of immutable Python Objects.
eg: egTuple = ('Faisal', 1994, 23.9).
Slicing on tuples with wrong indexes doesn't give index out of bound error
"""
egTuple = ('Faisal', 1994, 23.9)

# Concatenation
egTuple += ('Hyder', 'Royal Cyber')
print(egTuple)

# Index
print(egTuple[0])
print(egTuple[-1])  # -ve index starts to read object from the last
# print(egTuple[4]) # index out of bound error
# print(egTuple[-5])  # index out of bound error

# Slicing
print(egTuple[0:2])  # slicing works with same logic here as well, that it excludes the upper range while slicing
print(egTuple[5:-15])
