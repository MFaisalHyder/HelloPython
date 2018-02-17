"""
It is most flexible data type in PYTHON
Stores value in Key Value pair.
egDictionary = {1: 'Programming Languages', 'first' : 'Java', 'second' : 'Python'}
"""

egDictionary = {1: 'Programming Languages', 'first': 'Java', 'second': 'Python'}
print(egDictionary)

# In case of duplicates, latest value wins
egDictionary = {1: 'Programming Languages', 'first': 'Java', 'second': 'Python', 'second': 'C#'}
print(egDictionary)

# Dictionary Methods
# index [KeyError if given wrong index]
# print(egDictionary[5])
print(egDictionary['second'])

# len()
print(len(egDictionary))

# key()
print(egDictionary.keys())

# values()
print(egDictionary.values())

# items() [same as value but prints complete key-value pair]
print(egDictionary.items())

# get(key) [similar to key access approach]
print(egDictionary.get('first'))
print(egDictionary.get(1))

# update()
egDictionary.update({'first': 'PL'})
print(egDictionary)

# pop() [ removes element wrt given key]
# print(egDictionary.pop('second'))
egDictionary.pop('second')
print(egDictionary)
