import os

# os.remove("01.md")

# print(dir(os))

# a = os.listdir()
# print(a)

# os.remove("/home/vipikuma/my_data/temp/python_prec/zzz.txt")

# ['folder1', 'folder2', 'datetimemod.py', 'indian_dummy_names.py', '__init__.py', 'move.py', 'recursion.py', 'reqmod.py', 'string_prec.py', 'decorators.py', 'generator.py', 'prac.py', 'virtualenv.py', 'github.com', '1_hello.py', 'copy_file.py', 'test.text', 'test.html', 'test.json', 'learn_json.py', '5_operators.py', '6_ifelse.py', '7_if_else_practice.py', '8_matchcase.py', '9_while.py', '10_jump_statements.py', '11_strings.py', '12_lists.py', '13_tuples.py', '14_sets.py', '15_dicts.py', '1_shell.sh', '16_file_handling.py', '2_variables.py', '17_functions.py', 'test.py', 'new.text', '__pycache__', '3_type_convert.py', '4_input.py', '19_errorhandle.py', '20_classes.py', 'test.xml', '21_class_Inheritance.py', '22_class_practice.py', '23_class_encapsulation.py', '24_class_operator_overloading.py', 'bars.py', '25_bar_mod.py', '26_osmod.py', '1.md', '27_comprehension.py', 'QNA.text', '28_inbuild_functions.py', '16_01_forloop.py']

# for x in a:
#     if x.endswith(".py"):
#         print(x)

# print(os.path.exists("/home/vipikuma/my_data/temp/python_prec/"))

# for x in a:
#     if os.path.isdir(x):
#         print(x)

# print(os.path.exists("/home/vipikuma/my_data/temp/python_prec/folder1"))
# print(os.path.isfile("/home/vipikuma/my_data/temp/python_prec/bars.py"))

# Task:
# Terminal:
    # * if user type ls it will list all the files of the dir
    # * if user type lsfolder it will list all the folders only
    # * if user type lsfiles it will list all the files only
    # * if user type exit stop the terminal

# while True:
#     command  = input("-->")
#     if command == "ls":
#         print(os.listdir())
#     elif command == "lsfolder":
#         data = os.listdir()
#         for x in data:
#             if os.path.isdir(x):
#                 print(x)
#     elif command == "lsfile":
#         data = os.listdir()
#         for x in data:
#             if os.path.isfile(x):
#                 print(x)
#     elif command == "pyfiles":
#         a = os.listdir()
#         for x in a:
#             if x.endswith(".py"):
#                 print(x)
#     elif command == "jsonfile":
#         a = os.listdir()
#         for x in a:
#             if x.endswith(".json"):
#                 print(x)
#     elif command == "exit":
#         break
#     else:
#         print("invalid command")

import sys
# print(sys.argv)

def buy_stocks():
    print('Buy stocks')

def sell_stocks():
    print('Sell stocks')

# buy_stocks()
# sell_stocks()

# python 26_osmod.py abc
# ['26_osmod.py', 'abc']

# operation = sys.argv[1]

# if operation == "buy":
#     buy_stocks()
# elif operation == "sell":
#     sell_stocks()


# students = [
#     {"name": "Aarav Sharma", "result": "Pass"},
#     {"name": "Ananya Gupta", "result": "Pass"},
#     {"name": "Rohan Verma", "result": "Fail"},
#     {"name": "Priya Singh", "result": "Pass"},
#     {"name": "Karan Mehta", "result": "Fail"},
#     {"name": "Neha Patel", "result": "Pass"},
#     {"name": "Arjun Kumar", "result": "Pass"},
#     {"name": "Sneha Joshi", "result": "Fail"},
#     {"name": "Vivek Rao", "result": "Pass"},
#     {"name": "Meera Nair", "result": "Pass"},
# ]

# name = input("Enter A name: ")

# name = sys.argv[1]

# for x in students:
#     if x["name"] == name and x["result"] == "Pass":
#         print("Passed")
