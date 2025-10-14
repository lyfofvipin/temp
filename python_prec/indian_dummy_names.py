indian_dummy_names = [
    "Aarav Sharma", "Veda Iyer", "Ishaan Patel", "Saanvi Kapoor", "Aditya Reddy",
    "Ananya Gupta", "Vikram Mehta", "Priya Rao", "Arjun Desai", "Neha Verma",
    "Rohit Singh", "Sneha Joshi", "Karan Shah", "Pooja Malhotra", "Sameer Agarwal",
    "Shreya Jain", "Rahul Yadav", "Kritika Choudhury", "Amit Kumar", "Rina Nair",
    "Ravi Mishra", "Tanya Kapoor", "Manish Gupta", "Swati Sharma", "Vishal Bhat",
    "Ayesha Khan", "Deepak Patil", "Tanvi Agarwal", "Siddharth Reddy", "Aarti Mehta",
    "Ankur Prasad", "Madhavi Rao", "Puneet Sharma", "Maya Verma", "Anil Kapoor",
    "Disha Patel", "Yash Rajput", "Kiran Das", "Divya Joshi", "Rajesh Saini",
    "Pallavi Singh", "Raghav Gupta", "Simran Bedi", "Nikhil Deshmukh", "Kavya Saxena",
    "Himanshu Kumar", "Neelam Kapoor", "Gaurav Tiwari", "Rekha Yadav", "Suman Nair", "Aarav Sharma"
]

ages = [25, 18, 29, 21, 25, 25, 30, 22, 19, 28, 20, 24, 25, 18, 21, 23, 27, 26, 20, 29, 20, 21, 23, 26, 24, 18, 28, 22, 27, 26, 22, 24, 23, 29, 20, 21, 25, 27, 29, 21, 23, 26, 20, 19, 22, 24, 28, 25, 23, 20, 45]

data = { x:y for x, y in zip(indian_dummy_names, ages) }
# print(data)

# Consider that the numbers are the Age
# Tasks:
# * Print Names with Age Using For Loop ex: Vipin: 24 and so on
# * Make a new list that has elements in group of name and age ex: ("vipin", 24), ... and so on
# * Remove all duplicate data from the Age List
# * Get all Names Above 20 years by combining the Age and Numbers
# * Get All Names Who Are Of 30 Years

# new_list = []

# for x, y in zip(indian_dummy_names, ages):
#     if y >= 20:
#         new_list.append((x, y))

# new_list = [ f"{x}:{y}" for x, y in zip(indian_dummy_names, ages) if y > 20 ]
# print(new_list)

# age = 14

# data = "yes" if age >= 18 else "no"

# print(data)

# new_list = list(set(ages))
# print(new_list)

# for x in range(50):
#     print( f"{indian_dummy_names[x]} : {ages[x]}")

# ("arav", 25)

# new_list = []

# for x, y in zip(indian_dummy_names, ages):
#     new_list.append((x, y))

# print(new_list)

# new_list = [ f"{x}:{y}" for x, y in zip(indian_dummy_names, ages) ]
# print(new_list)

# [ print(x.upper()) for x in indian_dummy_names ]

# [ what_is_it_we_want_to_do_with_our_variable_name for variable_name in iterator ]


# print(
#     [ x[0] for x in indian_dummy_names ]
# )

# x = "Aarav Sharma"
# y = x.upper()
# print(y)

# a = [ 1, 5, 1, 4, 1 ]

# b = a.sort()

# print(a)
# print(b)

# data = []
# for i in range(1, 11):
#     data.append(i * i)
# print(data)

# print( list( x * x for x in range(1, 11) ) )

# [ x*x for x in range(1, 11) ]

# data = { x:y for x, y in zip(indian_dummy_names, ages) }

# print(data)


# data = {'Aarav Sharma': 45, 'Veda Iyer': 18, 'Ishaan Patel': 29, 'Saanvi Kapoor': 21, 'Aditya Reddy': 25, 'Ananya Gupta': 25, 'Vikram Mehta': 30, 'Priya Rao': 22, 'Arjun Desai': 19, 'Neha Verma': 28, 'Rohit Singh': 20, 'Sneha Joshi': 24, 'Karan Shah': 25, 'Pooja Malhotra': 18, 'Sameer Agarwal': 21, 'Shreya Jain': 23, 'Rahul Yadav': 27, 'Kritika Choudhury': 26, 'Amit Kumar': 20, 'Rina Nair': 29, 'Ravi Mishra': 20, 'Tanya Kapoor': 21, 'Manish Gupta': 23, 'Swati Sharma': 26, 'Vishal Bhat': 24, 'Ayesha Khan': 18, 'Deepak Patil': 28, 'Tanvi Agarwal': 22, 'Siddharth Reddy': 27, 'Aarti Mehta': 26, 'Ankur Prasad': 22, 'Madhavi Rao': 24, 'Puneet Sharma': 23, 'Maya Verma': 29, 'Anil Kapoor': 20, 'Disha Patel': 21, 'Yash Rajput': 25, 'Kiran Das': 27, 'Divya Joshi': 29, 'Rajesh Saini': 21, 'Pallavi Singh': 23, 'Raghav Gupta': 26, 'Simran Bedi': 20, 'Nikhil Deshmukh': 19, 'Kavya Saxena': 22, 'Himanshu Kumar': 24, 'Neelam Kapoor': 28, 'Gaurav Tiwari': 25, 'Rekha Yadav': 23, 'Suman Nair': 20}

# print( data["Aarav Sharma"] )
