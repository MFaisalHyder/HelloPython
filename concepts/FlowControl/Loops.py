"""
for, while, and other traversing techniques
"""

num1 = 10
num2 = 25

# while [while 'condition' : program code]
while num2 > num1:
    print("num2 is grater than num 1")
    num2 -= 1

# for [for 'iterator variable' in 'sequence' : program code]
myTuple = ('faisal', 1, 2, 3)
mySet = {1, 5, 6, 0, 2, 1, 'Faisal', 'Hyder', 'Hyder', 'Developer'}

for temp in mySet:  # myTuple:
    print(temp)

# break
count = 'a'
while True:
    print(count)
    count += count
    if len(count) > 10:
        break

# continue [continue to iterate without executing code written after continue]
for temp in range(25):
    if temp % 2 == 0:
        continue
    print(temp)
