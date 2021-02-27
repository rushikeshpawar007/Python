#Functions with output

def format_name(f_name, l_name):
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  return f"{formated_f_name} {formated_l_name}"


print(format_name('RuShIkEsH', 'PaWaR'))

#Multiple Return Values
def format_name(f_name, l_name):
  if f_name == '' or l_name == '':
    return 'Your input is not right'
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  return f"{formated_f_name} {formated_l_name}"


print(format_name(input('What is your first name? '), input('What is your last name? ')))


#day 10 - 1
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
  if month > 12 or month < 1:
    return 'Invalid month'
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  if is_leap(year) and month == 2:
    return 29
  return month_days[month - 1]

#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)


#calculator prototype



#Calculator


#Add
def add(n1, n2):
  return n1 + n2


#substract
def substract(n1, n2):
  return n1 + n2

#Multiply
def Multiply(n1, n2):
  return n1 * n2


#divide
def divide(n1, n2):
  return n1 + n2

operations = {
  '+': add,
  '-': substract,
  '*': Multiply,
  '/': divide
  }

num1 = int(input("What's the first number?: ")) 
num2 = int(input("What's the second number?: "))

for operation in operations:
  print(operation)


operation_sysmbol = input("Pick an operation from the line above: ")

calculation_function = operations[operation_sysmbol]
first_ans = calculation_function(num1, num2)

print(f'{num1} {operation_sysmbol} {num2} = {first_ans}')

#input("Type 'y' to keep calculating with {first_ans} or type 'no' to exit. ")
operation_sysmbol = input("Pick an operation from the line above: ")

num3 = int(input("What's the other number?: "))
calculation_function = operations[operation_sysmbol]
second_ans = calculation_function(calculation_function(num1, num2), num3)

print(f'{first_ans} {operation_sysmbol} {num3} = {second_ans}')



#final calculator
#Calculator
from art import logo
#Add
def add(n1, n2):
  return n1 + n2

#substract
def substract(n1, n2):
  return n1 + n2

#Multiply
def Multiply(n1, n2):
  return n1 * n2

#divide
def divide(n1, n2):
  return n1 + n2

operations = {
  '+': add,
  '-': substract,
  '*': Multiply,
  '/': divide
  }

def calculator():
  print(logo)
  num1 = float(input("What's the first number?: ")) 

  for operation in operations:
    print(operation)

  should_continue = True
  while should_continue:
    operation_sysmbol = input("Pick an operation from the line above: ")
    num2 = float(input("What's the second number?: "))
    calculation_function = operations[operation_sysmbol]
    ans = calculation_function(num1, num2)

    print(f'{num1} {operation_sysmbol} {num2} = {ans}')

    if input("Type 'y' to keep calculating with {ans} or type 'no' to exit. ") == 'y':
      num1 = ans
    else:
      should_continue = False
      calculator()
      
calculator()
  












