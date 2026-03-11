# import os

# # files = os.listdir()

# # for x in files:
# #     if os.path.isfile(x):
# #         print(x)

# # print(os.path.exists("/home/vipikuma/Downloadsss"))

# # print(os.path.isdir("/home/vipikuma/classes/python_afternoon_batch/break.py"))


# # Task:
# # Terminal:
#     # * if user type ls it will list all the files of the dir
#     # * if user type lsfolder it will list all the folders only
#     # * if user type lsfiles it will list all the files only

# while True:
#     command  = input("-->")
#     if command == "ls":
#         print(os.listdir())
#     elif command == "lsfolder":
#         data = os.listdir()
#         for x in data:
#             if os.path.isdir(x):
#                 print(x)
#     elif command == "lsfiles":
#         data = os.listdir()
#         for x in data:
#             if os.path.isfile(x):
#                 print(x)
#     elif command == "stop":
#         break
#     else:
#         print("invalid command")

# # import sys

# # print(sys.argv)



# # ls,
# # lsfolder,
# # lsfiles
# # stop
# # invalid command

# sticks = 21

# print("There are 21 sticks, you can take 1-4 number of sticks at a time.")
# print("Whoever will take the last stick will lose")

# while True:
#     print("Sticks left: " , sticks)
#     sticks_taken = int(input("Take sticks(1-4):"))
#     if sticks == 1:
#         print("You took the last stick, you lose")
#         break
#     if sticks_taken >= 5 or sticks_taken <= 0:
#         print("Wrong choice")
#         continue
#     print("Computer took: " , (5 - sticks_taken) , "\n")
#     sticks -= 5
