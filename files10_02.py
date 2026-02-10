# fd = open("test.txt")
# print(fd.read())

#mode
#r - read
#w - write
#a - append
#r+ = read + write
#w+ = write + read
#x = exclusive 

# fd = open("test.txt", "a" )
# fd.write("\nHello world")

# fd = open("test.txt", mode="r+")
# print(fd.tell()) #file position
# print(fd.read(5))
# print(fd.tell())
# fd.seek(10)
# print(fd.read(5))
# fd.write("Hello world")

# fd = open("test.txt", "r+") #mode = a
# print(fd.read(-2))
# # fd.seek(5)
# # print(fd.write("hello world"))

# import os
# os.system("cls")

fd = open("test.txt", "a")
# print(len(fd.readline()))
# print(fd.readline(36))

# print(fd.readlines())
# fd.close()

fd.writelines(['\nhello', '\nworld'])

