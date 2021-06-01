# def csv_reader(file_name):
#     for row in open(file_name):
#         yield row


# csv_gen = csv_reader("data.csv")
# csv_gen = (row for row in open('data.csv')) #() for generator expression
# row_count = 0

# for row in csv_gen:
#     print(row)
#     row_count += 1


# print(f"Row count is {row_count}")



#generating infinite sequence using generators

def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

def is_palindrome(num):
    # Skip single-digit inputs
    if num // 10 == 0:
        return False
    temp = num
    reversed_num = 0

    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp = temp // 10

    if num == reversed_num:
        return num
    else:
        return False

for i in infinite_sequence():
     pal = is_palindrome(i)
     if pal:
         print(pal)