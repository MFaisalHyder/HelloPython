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

# Type Specific functions

# append(value) [It takes only one argument i.e. value itself and adds it at the last]
list = [1, 2, 'many']
list.append('one to one')
print(list)

# extend(list) [It also takes only one argument either element or list]
list.extend('join')  # If extended value is in string and more than one characters then it breaks it down as list
list.extend(['many', 2, 1.0])
print(list)

# insert() [It takes exact two arguments, first index, and second value]
list.insert(4, 'few')  # It doesn't replace previous value instead just add new value at specified index and updates it
print(list)

# pop() [Removes last element from the list]
list.pop()
print(list)
