# fruits = ['Apple', 'Peach', 'Pear']
# for fruit in fruits:
#   print(fruit)
#   print(fruit + 'pie')
#   print(fruits)

# for number in range(1,11,2):
#   print(number)


total = 0
for number in range(1,101):
  total += number
print(total)

#You are going to write a program that calculates the average student height from a List of heights. 
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
tota_height = 0
for student in student_heights:
  tota_height += student
total_height = round(tota_height / n)
print(total_height)

#You are going to write a program that calculates the highest score from a List of scores. 
# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

highest_score = 0
for student in student_scores:
  highest_score > student
  highest_score = student
print(f'The highest score is {highest_score}')


#You are going to write a program that calculates the sum of all the even numbers from 1 to 100. Thus, the first even number would be 2 and the last one is 100:
total = 0
for number in range(2,101,2):
  total += number
print(total)

#You are going to write a program that automatically prints the solution to the FizzBuzz game.
for number in range(1,101):
  if number % 3 == 0 and number % 5 == 0:
    print('FizzBuzz')
  elif number % 3 == 0:
    print('Fizz')
  elif number % 5 == 0:
    print('Buzz')
  else:
    print(number)

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password = []

for letter in range(1,nr_letters + 1):
   random_char = random.choice(letters)
   password += random_char

for sysmbol in range(1,nr_symbols + 1):
   random_char = random.choice(symbols)
   password += random_char

for sysmbol in range(1,nr_numbers + 1):
   random_char = random.choice(numbers)
   password += random_char

random.shuffle(password)
# listToStr = ''.join(map(str, password)) 
# print(f'Your password is {listToStr}')

password_list = ''
for char in password:
  password_list += char
print(f'Your password is:  {password_list}')

