# File Handling Basics

# File handling in Python allows your programs to read data from and write data to files
# on your computer's storage. 
# This is essential for storing information permanently, 
# so it isn't lost when your program finishes.

# The open() Function

# name = input("Enter Your Name: ")
# age = input("Enter Your age: ")
# number = input("Enter Your number: ")

# The first step to working with any file is to open it.
# You do this using the built-in open() function. 
# It returns a file object, which is what you'll use to read or write data.

# The open() function takes two main arguments:
#     File Path: The location of the file on your computer (e.g., 'data.txt').
#     Mode: A character that specifies how you want to interact with the file.

# Mode	Character	Description
# Read	'r'	Opens the file for reading. (Default mode)
# Write	'w'	Opens the file for writing. Creates the file if it doesn't exist or overwrites it if it does.
# Append 'a' Opens the file for writing. Creates the file if it doesn't exist or adds to the end of the file if it does.

# a = open("test.text")
# print(a.readable())
# a.close()


# with open("test.text") as a:
#     print(a.readable())
#     a.read()

# data = [ "line1\n", "line2\n", "line3\n" ]

# a = open("test.text", "a")

# # print(a.write(data))
# a.writelines(data)

# a.close()


# a = open("/home/vipikuma/abcd_video.mp4", "ab")

# print(a.read())

# a.close()

# a = open("test.text", "w+")

# a.write("sadjasudhfiusahfdiusafd")

# print(a.readable())
# print(a.writable())

# a.close()

# with open("/home/vipikuma/abcd_video.mkv") as video_file:
#     print(video_file.readable())






# file_data = xyz.readline()
# print(file_data)

# with open("/home/vipikuma/test.png", "rb") as a:
#     photo = a.read()

# with open("/home/vipikuma/test1.png", "wb") as a:
#     a.write(photo)

# file_to_copy = input("Enter Your file name you want to copy: ")
# file_to_paste = input("Enter the new filename: ")

# with open(file_to_copy) as a:
#     data = a.read()

# with open(file_to_paste, "w") as a:
#     a.write(data)

# with open("test.text") as a:
#     data = a.read()

# countre_space = 0
# countre_new_line = 0
# for x in data:
#     if x == "\n":
#         countre_new_line += 1

#     if x == " ":
#         countre_space += 1

# print(countre_space, countre_new_line)

# print(len(data))
# Open a file named 'example.txt' in write mode

# /home/vipikuma/classes/python_afternoon_batch/folder2/dummy.tt -> Absolute Path
# folder2/dummy.tt -> Relative Path

# file_object = open('folder2/dummy.tt')
# file_object = open('folder2/dummy.tt', "r")

# print(file_object.read())

# print(file_object.readline())
# print(file_object.readline())

# print(file_object.readlines())

# The write() Method

# To write content to a file, you use the write() method on the file object. It takes a string as an argument.


# file_object = open('folder2/dummy.tt', "w")
# from indian_dummy_names import data
# file_object.write("""
# hi
#                   my
#                   name
#                   is
#                   vipin
#                   and
#                   this
#                   is 
#                   write 
#                   method""")

# file_object.writelines( [ f"{str(x)}\n" for x in range(1, 111) ] )

# for x in data.items():
#     file_object.write( f"{x[0]} age {x[1]}\n" )

# file_object.writelines( [ f"{x[0]} age {x[1]}\n" for x in data.items() ] )

# The close() Method

# After you finish your work with a file, you must close it to free up system resources. If you don't, changes might not be saved, or the file could be locked by your program.
# file_object = open('example.txt', 'w')
# file_object.write("Hello, World!\n")
# file_object.close()

# with open("folder2/dummy.tt", "w") as x :
#     print(x.readable())
#     print(x.writable())


# Append Mode

# with open("folder2/dummy.tt", "a") as x :
#     x.writelines([ f"{str(x)}\n" for x in range(50, 61) ])

# with open("/home/vipikuma/Pictures/pics/PXL_20231127_192054699.NIGHT.jpg", "+wb") as x :
#     # x.writelines([ f"{str(x)}\n" for x in range(50, 61) ])
#     print(x.read())

# with open("test.text") as f:
#     content = f.read()
#     print(f.newlines)

# r
# w
# a
# +r
# +w
# +a
# rb
# wb
# ab
# +rb
# +wb
# +ab
