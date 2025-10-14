# What is a Set?

# Imagine a bag where you throw in items, but if you try to put in something that's already there,
# It just gets ignored. Also, the items don't stay in any particular order. That's a Python set.

# Unordered: They don'e have any index values and they do not support slicing.
# Mutable: You can add or remove elements after the set has been created.
# Unique Elements: Every element in a set must be unique. Duplicates are automatically discarded.
# Heterogeneous: Sets can contain elements of different data types, but all elements must be hashable 
# (e.g., numbers, strings, tuples, but not lists or dictionaries).

# # Creating an empty set
# empty_set = set()
# print(f"Empty set: {empty_set}, type: {type(empty_set)}") # Output: Empty set: set(), type: <class 'set'>

# Creating a set from a list (duplicates are automatically removed)
# numbers_list = [1, 2, 3, 2, 4, 1, 5]
# my_set = set(numbers_list)
# print(f"Set from list (duplicates removed): {my_set}") # Output: Set from list (duplicates removed): {1, 2, 3, 4, 5} (order may vary)

# my_set = set((1, 3, 4, 5, 1, 4))
# print(my_set)

# Creating a set directly with curly braces
# fruits = {"apple", "banana", "cherry", "Banana", 1, 3, 4, 5, 1}
# print(f"Set of fruits: {fruits}") # Output: 
# dummy = {"x", "t", "a", "A", "X", "T"}
# print(dummy)

# sorted_data = sorted(dummy)
# print(sorted_data)

# Set with mixed data types (all elements must be hashable)
# mixed_set = {1, "hello", (1, 2), 3.14, (1, 2)} # Tuple is hashable
# print(f"Mixed set: {mixed_set}") # Output: Mixed set: {(1, 2), 1, 3.14, 'hello'} (order may vary)

# my_set = {1, 2, 3}
# print(f"Original set: {my_set}")

# my_set.add(4)
# print(f"After add(4): {my_set}") # Output: After add(4): {1, 2, 3, 4}

# my_set.add(2) # 2 is already in the set, no change
# print(f"After add(2): {my_set}") # Output: After add(2): {1, 2, 3}

# my_set.update([1, 2, 3, 4, 5, 6]) # 2 is ignored, 5 and 6 are added
# print(f"{my_set}") # Output: {1, 2, 3, 4, 5, 6}

# my_set.update("abcdefg") # 2 is ignored, 5 and 6 are added
# print(f"{my_set}") # Output: {1, 2, 3, 'a', 'c', 'g', 'f', 'd', 'e', 'b'}

# my_set.update({7, 8}) # Can update from another set
# print(f"After update({7, 8}): {my_set}") # Output: After update({7, 8}): {1, 2, 3, 4, 5, 6, 7, 8}


# my_set = {10, 20, 30, 40, 50}
# print(f"Original set: {my_set}")

# my_set.remove(30)
# print(f"{my_set}") # Output: After remove(30): {10, 20, 40, 50} (order may vary)

# my_set.discard(10)
# print(f"After discard(20): {my_set}") # Output: After discard(20): {10, 40, 50} (order may vary)

# pop method in list take an argument but in set there are no argument required

# data = my_set.pop()
# print(my_set)
# print(data)

# popped_item = my_set.pop()
# print(f"Popped item (arbitrary): {popped_item}, Set: {my_set}")

# my_set.clear()
# print(f"After clear: {my_set}") # Output: After clear: set()

# a = {1, 2, 3}
# b = a.copy()
# b.add(23)
# print(a)
# print(b)

# my_set = {10, 20, 30, 40, 50}

# # Membership
# print(f"Is 3 in my_set? {3 in my_set}")     # Output: Is 3 in my_set? True
# print(f"Is 6 not in my_set? {6 not in my_set}") # Output: Is 6 not in my_set? True

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# # Union
# union_set = set_a | set_b
# print(f"Union (set_a | set_b): {union_set}") # Output: Union (set_a | set_b): {1, 2, 3, 4, 5, 6}
# print(f"Union (set_a.union(set_b)): {set_a.union(set_b)}")

# Intersection
# intersection_set = set_b & set_a
# print(f"Intersection (set_a & set_b): {intersection_set}") # Output: Intersection (set_a & set_b): {3, 4}
# print(f"Intersection (set_a.intersection(set_b)): {set_a.intersection(set_b)}")

# Difference (elements in A but not in B)
# difference_ab = set_a - set_b
# print(f"Difference (set_a - set_b): {difference_ab}") # Output: Difference (set_a - set_b): {1, 2}
# print(f"Difference (set_a.difference(set_b)): {set_a.difference(set_b)}")

# Difference (elements in B but not in A)
# difference_ba = set_b - set_a
# print(f"Difference (set_b - set_a): {difference_ba}") # Output: Difference (set_b - set_a): {5, 6}

# set1 = {1, 2, 3}
# set2 = {1, 2, 3, 4, 5}
# set3 = {4, 5, 6}

# Is set1 a subset of set2?
# print(f"Is {set1} subset of {set2}? {set1.issubset(set2)}") # Output: True
# print(f"Is {set1} <= {set2}? {set1 <= set2}") # Output: True

# Is set2 a superset of set1?
# print(f"Is {set2} superset of {set1}? {set2.issuperset(set1)}") # Output: True
# print(f"Is {set2} >= {set1}? {set2 >= set1}") # Output: True

# Are set1 and set3 disjoint? (No common elements)
# print(f"Are {set1} and {set3} disjoint? {set1.isdisjoint(set3)}") # Output: True

# # Are set1 and set2 disjoint?
# print(f"Are {set1} and {set2} disjoint? {set1.isdisjoint(set2)}") # Output: False (they share 1, 2, 3)


# Create a frozenset
# In frozenset You Can not add, update, remove, pop, discard

# fs = frozenset([1, 2, 3])
# fs2 = frozenset([1, 2, 3])
# print(type(fs)) # Output: Frozenset: frozenset({1, 2, 3})
