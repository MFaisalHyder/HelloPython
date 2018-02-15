""""
List is a sequence of mutable Python objects. i.e. values at indexes can be re assigned.
eg: egList = ['Muhammad', 'Faisal', 'Hyder', 1994, 05, 23.9]
"""

egList = ['Muhammad', 'Faisal', 'Hyder', 1994, 'May', 23.9]
print(egList)

# Mutability
egList[4] = 5  # we cant do the same with Tuples
print(egList)

# Concatenation
egList += ['Software Engineer', 1.2]
print(egList)

# Index
print(egList[0])
print(egList[0o5])
print(egList[-4])

# Slicing
print(egList[2:4])  # prints item at index 2, and item at max index - 1 (i.e. 4-1)
print(egList[3:-6])

# Repetition
print(egList * 2)
