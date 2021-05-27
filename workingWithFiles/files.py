# writing this file this way we need to manually close the file
# file = open('some.txt','a')
# file.write('some thing is too')
# file.close()

#writing this way closes file automatically
# with open('new.txt','a') as file:
#     data='something is too much.'
#     file.write(data)


#writing text file
with open('new.txt','a') as f:
    f.write('al')
    print(type(f))

#writing files as binary
with open('binary.txt','wb') as f:
    f.write(bytearray('stinrg','utf-8'))
    print(type(f))



# reading this file 
with open("new.txt",'r') as file:
    for lines in file:
        print(lines)
    


