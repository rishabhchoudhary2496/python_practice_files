#strings are immutable data type

movie = 'Tenent'
print('movie\
    this\
')

print(movie)

#raw string characters are not escaped even when using special characters
print(R'foo\\bar')
print('Hi'*4)

print(movie[1])
print(movie[-1]) #reverse order

#slicing strings in python
print(movie[3:-2])
char = 'professor'
#del char
print(char)

print('hello'+'world')

#iterating a string 
for i in movie:
    print(i)

#substring test in string
print('e' in movie)

print(movie[::-1])

#string methods
print(movie.capitalize()) #uppercase
print(movie.casefold())  #lowercase
print(movie.center(10))  #center string taking width
print(movie.count('en'))  #number of substring occurrence in string
print(movie.endswith('t'))  #check if string ends with certain character
print(movie.find('e')) #find char position in string
print(movie.index('en')) #index position of substring
print(movie.isalpha())
print(movie.isalnum())
print(movie.isdigit())
print(movie.isidentifier())
print(movie.islower())
print(movie.split(' '))
print(movie.startswith('T'))
print(movie.zfill(10))


#string interplotion in python
actor = 'racheal weisz' 
movie = 'The Mummy'
#using fstrings#
print(f'{actor} acted in {movie} series') 

#% formatting method 
print('%s actress in %s' %(actor,movie))

#str.format method
print('{} acted in {}'.format(actor,movie))
