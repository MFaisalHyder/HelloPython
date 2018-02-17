"""
It is most flexible data type in PYTHON
Stores value in Key Value pair.
egDictionary = {1: 'Programming Languages', 'first' : 'Java', 'second' : 'Python'}
"""

egDictionary = {1: 'Programming Languages', 'first': 'Java', 'second': 'Python'}
print(egDictionary)

# In case of duplicates, latest value wins
egDictionary = {1: 'Programming Languages', 'first' : 'Java', 'second' : 'Python', 'second' : 'C#'}
print(egDictionary)