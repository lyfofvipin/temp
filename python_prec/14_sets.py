# What is a Set?

# Imagine a bag where you throw in items, but if you try to put in something that's already there,
# It just gets ignored. Also, the items don't stay in any particular order. That's a Python set.

# Unordered: They don'e have any index values and they do not support slicing.
# Mutable: You can add or remove elements after the set has been created.
# Unique Elements: Every element in a set must be unique. Duplicates are automatically discarded.
# Heterogeneous: Sets can contain elements of different data types, but all elements must be hashable 
# (e.g., numbers, strings, tuples, float but not lists or dictionaries).
# While 1 and True are the same thing
# While 0 and False are the same thing

# Creating an empty set
# empty_set = set()
# print(empty_set, type(empty_set))

# a = { 1, 2, 3, 4, 5, 6, 1, 2, "Vipin", "vipin", True, 0, False }
# print(a)

# Creating a set from a list (duplicates are automatically removed)
# numbers_list = "Rajasthan"
# my_set = set(numbers_list)
# print(f"Set from list (duplicates removed): {my_set}")

# my_set = set((1, 3, 4, 5, 1, 4))
# print(my_set)

# Creating a set directly with curly braces
# fruits = {"apple", "banana", "cherry", "banana", 1, 3, 4, 5, 1}
# print(f"Set of fruits: {fruits}")
# dummy = {"x", "t", "a", "A", "X", "T"}
# print(dummy)

# Set with mixed data types (all elements must be hashable)
# mixed_set = {1, "hello", (1, 2), 3.14, (1, 2)} # Tuple is hashable
# print(f"Mixed set: {mixed_set}")

# my_set = {1, 2, 3}
# print(f"Original set: {my_set}")

# Add and Update method works separately in a way that add can only insert immutable data types
# update method can expend the datatype and add it also it can add mutable datatypes.
# remove method will give an error if we pass it a element which does not exist and discard will not

# my_set.add((1,2))
# print(f"After add(4): {my_set}")

# my_set.add(2) # 2 is already in the set, no change
# print(f"After add(2): {my_set}")

# my_set.update((1, 2, 3, 4, 5, 6)) # 2 is ignored, 5 and 6 are added
# print(f"{my_set}")

# my_set = {1 ,2 ,3}

# my_set.add("abcdefg")
# print(f"{my_set}") 

# my_set.add({7,8})
# print(my_set)

# my_set.update({7, 8}) # Can update from another set
# print(f"After update({7, 8}): {my_set}") # 

# my_set = {10, 20, 30, 40, 50}
# print(f"Original set: {my_set}")

# my_set.remove(90)
# print(f"{my_set}")

# my_set.discard(20)
# print(f"After discard(20): {my_set}")

# pop method in list take an argument but in set there are no argument required

# data = my_set.pop()
# print(my_set)
# print(data)

# popped_item = my_set.pop()
# print(f"Popped item (arbitrary): {popped_item}, Set: {my_set}")

# my_set.clear()
# print(f"After clear: {my_set}") # 

# a = {1, 2, 3}
# b = a.copy()
# b.add(23)
# print(a)
# print(b)

# my_set = {10, 20, 30, 40, 50}

# # Membership
# print(f"Is 3 in my_set? {3 in my_set}")     # 
# print(f"Is 6 not in my_set? {6 not in my_set}") # 

# set_a = {1, 2, 3, 4}
# set_b = {3, 4, 5, 6}

# new_set = set_a.union(set_b)
# new_set = set_a | set_b # Pipe Operator
# print( new_set)

# Intersection
# print(f"Intersection (set_a.intersection(set_b)): {set_a.intersection(set_b)}")
# intersection_set = set_b & set_a
# print(f"Intersection (set_a & set_b): {intersection_set}") # 

# set_a = {1, 2, 3, 4}
# set_b = {3, 4, 5, 6}

# # Difference (elements in A but not in B)
# difference_ab = set_b - set_a
# print(f"Difference (set_a - set_b): {difference_ab}") # 
# print(f"Difference (set_a.difference(set_b)): {set_b.difference(set_a)}")

# symmetric_difference
# It is same as Union but it will not count the element that comes in both the sets
# a = {1,2,3}
# b = {3,4,5}

# print( a, b, a.symmetric_difference(b) )
# print( set_b.symmetric_difference(set_a) )

# set1 = {1, 2, 3}
# set2 = {1, 2, 3, 4, 5}
# set3 = {4, 5, 6}
# set4 = { 8, 9 }

# Is set1 a subset of set2?
# print(f"Is {set1} subset of {set2}? {set1.issubset(set2)}")
# print(f"Is {set1} <= {set2}? {set1 <= set2}") 

# Is set2 a superset of set1?
# print(f"Is {set2} superset of {set1}? {set2.issuperset(set1)}") 
# print(f"Is {set2} >= {set1}? {set2 >= set1}") 

# Are set1 and set3 disjoint? (No common elements)
# print( set1.isdisjoint( set4 ) )
# print(f"Are {set1} and {set3} disjoint? {set1.isdisjoint(set3)}") 

# Are set1 and set2 disjoint?
# print(f"Are {set1} and {set2} disjoint? {set1.isdisjoint(set2)}") 

# Create a frozenset
# In frozenset You Can not add, update, remove, pop, discard
# fs = frozenset([1, 2, 3, 1, 1, 2, 3])
# ns = set([1, 2, 3, 1, 1, 2, 3])

# a = 43
# b = 456

# print( dir() )

# print( __name__ )

# print(ns.pop())
# fs2 = frozenset([1, 2, 3])
# print(type(fs)) 

# | Feature                  | List                | Tuple             | Set             | Frozenset     | String         |
# | ------------------------ | ------------------- | ----------------- | --------------- | ------------- | -------------- |
# | **Syntax**               | `[ ]`               | `( )`             | `{ }`           | `frozenset()` | `' '` or `" "` |
# | **Ordered**              | ✅ Yes              | ✅ Yes            | ❌ No           | ❌ No         | ✅ Yes         |
# | **Mutable** (can change) | ✅ Yes              | ❌ No             | ✅ Yes          | ❌ No         | ❌ No          |
# | **Duplicates allowed**   | ✅ Yes              | ✅ Yes            | ❌ No           | ❌ No         | ✅ Yes         |
# | **Indexing possible**    | ✅ Yes              | ✅ Yes            | ❌ No           | ❌ No         | ✅ Yes         |
# | **Elements type**        | Any                 | Any               | Only hashable   | Only hashable | Characters     |
# | **Use case**             | Dynamic collections | Fixed collections | Unique elements | Immutable set | Text data      |
