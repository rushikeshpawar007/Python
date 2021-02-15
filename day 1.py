message = 'Hello World'

print('Hello World')

print(message)


message = "Bobbie's World"

print(message)

message = """Bobbie's World was a great cartoon in 1990s"""

print(message)

#Length
message = 'Hello World'

print(len(message))

#slicing
message = 'Hello World'

print(message[10])

message = 'Hello World'

print(message[0:5])

message = 'Hello World'

print(message[:5])

message = 'Hello World'

print(message[6:11])


#method or function
message = 'Hello World'

print(message.lower())

message = 'Hello World'

print(message.upper())

message = 'Hello World'

print(message.find('World'))

message = 'Hello World'

message = message.replace('World','univerise')

print(message)


greeting = 'Hello'
name = 'Michael'

message = greeting + ', ' + name + '. Welcome' 

print(message)

#place holder
greeting = 'Hello'
name = 'Michael'

message = '{}, {} .Welcome.' .format(greeting, name) 

print(message)

greeting = 'Hello'
name = 'Michael'

message = f'{greeting}, {
name} .Welcome.' 
print(message)
