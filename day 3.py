#courses = ['History', 'Science', 'Maths','physics']
#courses_2 = ['Art','Education']
#nums = [1, 5, 4, 3]


#courses.append('Art')
#courses.insert(0,'Art')
#courses.insert(0,courses_2)

#courses.extend(courses_2)
#courses.append(courses_2)
#print(courses[0])
#print(courses[-1])
#print(courses[2])
#print(courses[1])

#print(courses[0:3])
#print(courses[:3])

#courses.remove('History')
#popped = courses.pop()

#courses.reverse()
#courses.sort(reverse=True)
#nums.sort(reverse=True)

#sorted_courses = sorted(courses)

#print(sorted_courses)
#print(min(nums))
#print(max(nums))
#print(sum(nums))

#print(courses.index('Maths'))
#print(courses.index('physics'))

#print('Arts' in courses)

#print('Maths' in courses)

#for item in courses:
#	print(item)

#for index, course in enumerate(courses, start=1):
#print(index, course)

#courses = ['History', 'Science', 'Maths','physics']

#course_str = ', '.join(courses)
#course_str = '-'.join(courses)

#new_list = course_str.split('-')
#print(course_str)
#print(new_list)

#list are mutable, Tuple are not

#Sets are random values 
cs_courses = {'History', 'Science', 'Maths','physics'}
art_course = {'History', 'Maths', 'Art', 'Design'}


print(cs_courses.intersection(art_course))
print(cs_courses.difference(art_course))
print(cs_courses.union(art_course))

# If Else statement

print('Welcome to the rollercoaster!')
height = int(input('What is your height in cm? '))

if height >= 120:
    print('You can go for the ride!')
    age = int(input('What is your age? '))
    if age > 18:
      print('you have to pay 12$')
    elif age >= 12:
      print('you have to pay 7$')
    else:
      print('you have to pay 5$')
else:
    print('Sorry, you need to grow taller to ride.')


# BMI calculator v.20
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = round(weight / height**2, 2)

print(bmi)

if bmi < 18.5:
    print(f'your bmi is {bmi}, you are underweight.')
elif bmi < 25:
    print(f'your bmi is {bmi}, you are normal weight.')
elif bmi < 30:
    print(f'your bmi is {bmi}, you are over weight.')
elif bmi < 35:
    print(f'your bmi is {bmi}, you are obse.')
else:
    print(f'your bmi is {bmi}, you are clinically obse.')


# Leap year
# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if year % 4 != 0:
  print('it is not a leap year')
elif year % 100 == 0:
  print('it is a leap year')
elif year % 400 == 0:
  print('it is a leap year')
else:
  print('it is not a leap year')


#pizza order
# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill = 0
s = 15
m = 20
l = 25

if size == s:
  bill = s
elif size == m:
  bill = m
else:
  bill = l

if add_pepperoni == 'Y':
  if size == s:
    bill += 2
  else:
      bill += 3

if extra_cheese == "Y":
  bill += 1
  
print(f"Your final bill is: ${bill}.")


