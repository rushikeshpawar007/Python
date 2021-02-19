# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is

Language = 'Java'

if Language == 'Python':
	print('Language is Python')
elif Language == 'Java':
	print('Language is Java')
else:
	print('Language is marathi')



course = 'Jeo'

if course == 'Science':
	print('the course is Science')

elif course == 'maths':
	print('the coourse is maths')

else:
	print('No match')

user = 'Admin'
logged_in = False

#if user == 'Admin' and logged_in:
#	print('Admin page')

#else:
#	print('bad creds')

if not logged_in:
	print('Admin Page')
else:
	print('bad creds')


# False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.

condition = False

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')


	import random

test_seed = int(input('create a seed number: '))
random.seed(test_seed)

random_side = random.randint(0,1)

if random_side == 1:
  print('Heads')
else:
  print('Tails')

  # Split string method
import random

test_seed = int(input('Create a Seed number: '))
random.seed(test_seed)
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
x = len(names)
final = random.randint(0, x - 1)
final_name = (names[final])
print(f'{final_name} has too pay the bill')



#randomisation
import random

random_integer = random.randint(1, 10)

print(float(random_integer))

random_float = random.random()
print(random_float)

love_score = random.randint(1,100)
print(f'YOur score is {love_score}')


states_of_america = ['rushikesh', 'pawar', 'aditya']

states_of_america.append('vaibhav')

print(states_of_america)