# File Handling Basics

# File handling in Python allows your programs to read data from and write data to files
# on your computer's storage.
# This is essential for storing information permanently, 
# so it isn't lost when your program finishes.

# The open() Function

# name = input("Enter Your Name: ")
# age = input("Enter Your age: ")
# number = input("Enter Your number: ")

# print( name, age, number )

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

# print(type(a))

# print( dir(a) )

# print(a.readable())

# print(a.read())

# data = a.read()
# print(data.upper())

# b = a.readline()
# print(b)
# c = a.readline()
# print(c)
# d = a.readline()
# print(d)

# print(a.read())

# print( b, c, d )

# print(a.readlines())

# b = a.read()

# a = open("test.text")
# print( b )

# "C:\Users\Dell\OneDrive\Pictures\Screenshots\data scince\python\formateed_string.py"
# a=open("/home/vipikuma/my_data/temp/python_prec/11_strings.py")
# a=open("12_forloop.py")
# print(type(a))

# a.close()

# with open("test.text") as a:
#     print(a.readable())
#     print(a.read())
#     print(a.writable())

# data = [ "line1\n", "line\n2", "line3", "sadfasfd\n", "ASDfae" ]

# a = open("test.text", "r")
# print(a.read())
# a.close()

# a = open("abcd.text", "w")
# print(a.readable())
# print( a.writable() )

# a.write( "I am from Jaipur." )

# a.writelines(data)

# a.close()


# with open("abcd.text", "w") as a:
#     a.write("I am from Delhi.")

# with open("abcd.text", "a") as a:
#     a.write( "I am from Delhi.\n" )

# print(a.write(data))
# a.writelines(data)

# a.close()


# a = open("/home/vipikuma/test.mp4", "wb")
# a.close()

# a = open("test.text", "w+")

# a.write("sadjasudhfiusahfdiusafd")

# print(a.readable())
# print(a.writable())

# a.close()

# with open("/home/vipikuma/abcd_video.mkv") as video_file:
#     print(video_file.readable())



# with open("abcd.text", "+a") as a:
#     print(a.readable())
#     print(a.writable())

# +r
# +w
# +a
# +rb
# +wb
# +ab

# file_data = xyz.readline()
# print(file_data)

# with open("/home/vipikuma/test.png", "rb") as a:
#     photo = a.read()

# with open("/home/vipikuma/test1.png", "wb") as a:
#     a.write(photo)

# file_to_copy =  input("Enter Your file name you want to copy: ")
# file_to_paste = input("Enter the new filename: ")

# with open(file_to_copy, "rb") as a:
#     data = a.read()

# with open(file_to_paste, "wb") as a:
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


# Create a file and write your name, age, and city into it.

# Make file and dump based on this file do below task:
"""
India is a beautiful country.
India is known for its rich culture.
India has many historical monuments.
India celebrates many festivals.
India is famous for its diversity.
India is located in South Asia.

India has a strong democracy.
India is the birthplace of yoga.
India has many different languages.
India is famous for delicious food.

India has a rich history.
India is known for the Taj Mahal.
India has the Himalayan mountains.
India is developing in technology.
India has a large population.

India is famous for cricket.
India has many rivers and forests.
India celebrates Independence Day proudly.
India has talented scientists and teachers.
India is respected around the world.

India has colorful traditions.
India is home to many religions.
India is progressing in space research.
India teaches unity in diversity.

India has hardworking people.
India has many tourist attractions.
India is famous for traditional clothing.
India has beautiful villages and cities.

India is a land of culture and peace.
India is a proud and great nation.
Jaipur is known as the Pink City.
Jaipur is the capital of Rajasthan.
Jaipur is famous for its palaces.

Jaipur attracts many tourists every year.
Jaipur has beautiful forts and temples.
Jaipur is known for traditional jewelry.
Jaipur has colorful markets.
Jaipur is famous for handicrafts.

Jaipur has rich Rajasthani culture.
Jaipur is a clean and beautiful city.
Jaipur is popular for delicious food.
Jaipur has many historical places.

Jaipur is one of the major cities of Rajasthan.
Jaipur is famous for Hawa Mahal.
Jaipur has grand celebrations during festivals.
Jaipur is loved by tourists from many countries.

Jaipur has modern buildings and roads.
Jaipur is known for its hospitality.

Jaipur is growing rapidly in education and business.
Jaipur is a proud city of Rajasthan.
"""

# Read a file and display only lines containing a word india.
# Write a program to count vowels in a text file.
# Reverse the contents of a file and save them into another file.
# Write a program to remove blank lines from a file.

# with open("new.text", "w") as new_file:

#     with open("test.text") as file:
#         data = file.read()
#         new_file.write(data[::-1])
        # new_file.write(data.replace("\n\n", ""))
        # for x in data:
        #     if x.strip() == "\n":
        #     # if x != "\n":
        #         new_file.write(x)
