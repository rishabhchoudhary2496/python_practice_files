# file = open('info.txt')
# print(file.tell()) #return character position of handler
# print(file.readline())
# file.seek(0)
# # print(file.tell()) #reset position of handler
# print(file.readline())
# file.close()


with open ('info.txt') as file:
    print(file.read(2))