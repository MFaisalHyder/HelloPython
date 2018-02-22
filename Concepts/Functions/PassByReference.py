""""
In Python functions are 'pass by Reference' i.e when we send arguments to a method
python sends its reference as a value in that argument not the variable(value) itself
"""


def world_clubs(clubs_list):
    # If we perform type specific operations on it then it performs changes over the referenced data
    # clubs_list.extend(['PSG', 'Sevilla', 'Dortmund'])

    # But here as we are assigning then the actual reference is not modified
    clubs_list = ['PSG', 'Sevilla', 'Dortmund']

    print("list with modified data..", clubs_list)


my_clubs = ['Real Madrid', 'Juventus', 'Bayern', 'Tott. Hotspur']
print("list before method call..", my_clubs)

# calling method to change this list sent as an argument
world_clubs(my_clubs)
print("list after method call..", my_clubs)
