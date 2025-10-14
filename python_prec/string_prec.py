# Palindrome Checker:

# data = "121"

# if data == data[ ::-1 ]:
#     print("It's a Palindrome")
# else:
#     print("It's Not a Palindrome")


# Sentence Word Counter:
# Ask the user to enter sentences one by one.
# Use a while loop to keep accepting input until the user types
# "STOP" (case-insensitive).
# For each sentence entered, use an if-else statement to check if the sentence contains more 
# than 5 words.
# Print the sentence and indicate if it's "Long sentence!" or "Short sentence!".
# (Hint: You can split the sentence into words using split() and then check the length of the resulting list).

# while True:

#     data = input("Enter Your Sentence: ")

#     if data.lower() == "stop":
#         break

#     if data.count(" ") + 1 >= 5:
#         print("It's a long statement.")
#     else:
#         print("It's a short statement.")

# Ask the user to type a string. Use a while loop to process characters one by one
# (you can iterate using an index that increments). Maintain counts for:

# Uppercase letters
# Lowercase letters
# Digits
# Special characters (anything else)

# Use if-elif-else statements to categorize each character
#  Stop the loop if you encounter the character '#'.
# Finally, print the counts for each type of character.

# count_upper = count_lower = count_digit = count_spl = 0

# data = "abcdsanfkjsabfASDFJKSAFDENREJ23y274627722387213478!#@(*!@(&#%(!@&%(@&%#(@!$#(@!&(#!&%&(!@&#(!@&%@#dhjbsh"
# length = len(data)

# counter = 0
# while counter < length:
    
#     if data[counter] in "abcdefghijklmnopqrstuvwxyz":
#         count_lower += 1
#     elif data[counter] in "1234567890": # "1".isnumeric()
#         count_digit += 1
#     elif data[counter] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
#         count_upper += 1
#     else:
#         count_spl += 1
#     counter += 1

# print( f"Count Of Lower Are {count_lower}, Count Of Upper are {count_upper}, Count Of Digits are {count_digit} and SPL char are {count_spl}" )

