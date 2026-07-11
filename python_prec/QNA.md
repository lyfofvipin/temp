# Python Learning Q&A

Practice questions organized to match the numbered lesson files (`1_hello.py` → `35_requests.py`).

---

## Table of Contents

1. [While Loop](#while-loop)
2. [Strings](#strings)
3. [Lists](#lists)
4. [Sets](#sets)
5. [Dictionaries](#dictionaries)
6. [Tuples](#tuples)
7. [Functions](#functions)
8. [Generators & Iterators](#generators--iterators)
9. [Decorators](#decorators)
10. [What to Learn Next (Expert Roadmap)](#what-to-learn-next-expert-roadmap)

---

## While Loop

> File: `9_while.py`

### Star Printing Patterns

```
* * * *
* * * *
* * * *
* * * *
```

```
*
* *
* * *
* * * *
* * * * *
```

```
* * * * *
* * * *
* * *
* *
*
```

```
        *
      * *
    * * *
  * * * *
* * * * *
```

```
    *
   * *
  * * *
 * * * *
* * * * *
 * * * *
  * * *
   * *
    *
```

### Real-Life Scenarios

---
**Reverse a Number**

Write a program that takes an integer input from the user (e.g., `1234`) and prints the number in reverse (`4321`) using a while loop and basic math operations (`%` and `//`).

---
**Vowel Counter**

Write a program that takes a string input from the user. Using a while loop, iterate through the string character by character and count how many vowels (`a`, `e`, `i`, `o`, `u`) it contains.

---
**Case Swapper**

Write a program that takes a string and creates a new string where all uppercase letters are converted to lowercase, and all lowercase letters are converted to uppercase. Use a while loop to process each character.

Example: Input `"PyThOn"` → Output `"pYtHoN"`

---
**Secure Password Validator**

Write a program that forces a user to enter a secure password. The while loop should keep asking for input until the user provides a string that meets all of these criteria:

- At least 8 characters long
- Contains at least one digit (`0-9`)
- Contains at least one special character (like `$`, `#`, or `@`)

---

## Strings

> File: `12_strings.py`

### Real-Life Scenarios

---
**Email Cleanup**

A user is registering on your website and accidentally types their email with extra spaces: `email = "   alex@gmail.com   "`. Write code to clean this input and extract only the valid email ID.

---
**HTTPS Verification**

You are building a secure web crawler. Given `url = "https://xyz.com"`, write a line of code to verify if the website protocol starts with `"https"`.

---
**Log File Cleanup**

A Python script needs to clean up server log files. Given `log_entry = "[ERROR]===System Crash==="`, write a line of code to strip away only the trailing `=` characters from the right side.

---
**File Extension Check**

A user uploads a file named `document = "final_report.pdf"`. Write code to check if this file ends with the appropriate `.pdf` extension.

---
**Search Case Normalization**

A user searches for `"IPHONE"`, but the database holds the item as `"iphone"`. Write code to convert the user's search string so it matches the database, regardless of case.

---
**Receipt Price Alignment**

The price of an item is `price = "450"`. Write code to right-justify this price inside a 10-character wide block so it aligns with other receipts.

---
**Profanity / Word Replacement**

A user submits: `msg = "This software has a nasty bug"`. Write code to automatically replace the word `"bug"` with `"feature"`.

---
**Comment Line Detection**

Given `line = "# This is a comment line"`, write code to check if the line starts with a comment symbol.

---
**Domain Prefix Removal**

An API returns `domain = "www.google.com"`. Write a single line using a strip method to remove the `"www."` prefix.

---
**Scoreboard Zero Padding**

The current score is `score = "75"`. Write code to pad it with leading zeros so it displays as a 5-digit number (`00075`).

---
**URL Slug Generation**

Given `title = "blue running shoes"`, write code to replace all spaces with dashes to produce `"blue-running-shoes"`.

---
**API Key Newline Cleanup**

A script reads an auth key with a trailing newline: `key = "KEY123XYZ\n"`. Write a line of code to clean this string so only `"KEY123XYZ"` remains.

---
**Server Name Formatting**

Given `server = "sub-domain-01"`, write code to convert the name into uppercase letters.

---
**Immutability Prediction**

Look at this code:

```python
username = "guest123"
username.upper()
print(username)
```

Predict exactly what will print and explain why `username` did not change.

---
**Spam Filter — Find Word Position**

Given `email_body = "Get rich quick! Click here now!"`, write code using a string method to check if `"Click"` exists and get its starting position.

---
**Word Frequency in Document**

Given `paragraph = "Python is great because python code is easy to read"`, write code to count how many times the lowercase word `"python"` appears.

---
**Username Validation**

The system requires usernames with only letters and numbers. Given `username = "coder_99"`, write code to check if it fits this rule.

---
**Birth Year Validation**

Given `birth_year = "2005"`, write a line of code to verify if the string consists entirely of numbers before converting to integer.

---
**Title Case Formatting**

Given `blog_title = "10 tips for learning python"`, write code to capitalize only the first letter of the sentence.

---
**Shouting Detection**

Given `chat = "HELP ME PLEASE!!"`, write code to check if all alphabetical characters in the message are uppercase.

### Strings Only — No Loops

- How do you reverse a string using only slicing?
- Write a program to convert the first letter of a string to uppercase and the rest to lowercase.
- How do you find the total number of characters in a string?
- How do you count how many times the letter `"a"` appears without using a loop?
- Given `"Jaipur"`, how do you extract just the first three characters (`"Jai"`)?
- How do you check if a string ends with `"ing"` without using a loop?
- How do you replace all spaces in a string with hyphens?
- How do you check if a string contains only numbers?
- How do you find the starting index of the word `"Python"` inside a longer sentence?
- How do you check if a string is a palindrome using slicing?

### Basic Level (With Loops)

- Write a program to print each character of a string on a new line using a loop.
- Write a program to reverse a given string using a for loop.
- Write a program to count the total number of vowels in a string using a loop.
- Write a program to find and print the total number of spaces inside a string.
- Write a program to copy one string into another character by character using a loop.

### Intermediate Level

- Write a program to check whether a given string is a palindrome using loops.
- Write a program to extract and print only the numerical digits from a mixed string.
- Write a program that converts every alternate character to uppercase (e.g., `"python"` → `"PyThOn"`).
- Write a program to count how many times a specific character appears without using `.count()`.
- Write a program to remove all duplicate characters from a string using loops.

### Advanced Level

- Write a program to find the first non-repeating character using nested loops.
- Write a program to check if a string contains only alphabetic characters without using `.isalpha()`.
- Given two strings of equal length, merge them by alternating characters (e.g., `"ABC"` + `"xyz"` → `"AxByCz"`).
- Write a program to find the longest word in a sentence using a loop.
- Write a program to count the number of words in a sentence by detecting spaces with a loop.

---

## Lists

> File: `13_lists.py`

### Real-Life Scenarios

---
**UI Undo Feature & List References**

You are coding an undo feature for a drawing app:

```python
current_actions = ["line", "circle", "square"]
backup_actions = current_actions
current_actions.append("triangle")
```

If you print `backup_actions`, will it contain `"triangle"` or not? Explain what happens in Python's memory.

---
**E-Commerce Cart Slicing**

Given `cart = ["shoes", "shirt", "watch", "hat", "belt", "socks"]`, write a single line using negative list slicing to extract exactly the last 3 items.

---
**Inventory Sorting & Case Sensitivity**

A warehouse runs `.sort()` on `tags = ["banana", "Vipia", "apple", "cherry", "vipin"]`. Write down exactly what the list looks like after sorting and explain how capital letters affect order.

---
**IoT Sensor Data Extraction**

Given `numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`, write a slice expression that retrieves every 4th element starting from index 0.

---
**Social Media Notification Feed**

Given `notifications = ["Like", "Comment"]`, write the exact code to add `"New Follower"` to the beginning of the list.

---
**Deep Destructuring of Package Logs**

```python
log_data = ["Vipin", 25, "Jaipur", 302020, True, ["Test", 43, [23242, [234234]]]]
```

Write a single print statement to extract the innermost integer `234234`.

---
**Banking Ledger: Append vs Extend**

A banking app has `ledger = [100, -50, 200]` and a batch `new_batch = [500, -20, 30]`.

- Predict what `ledger` looks like after `ledger.append(new_batch)`.
- Predict what `ledger` looks like after `ledger.extend(new_batch)`.

### No Loops Allowed

- How do you access and print the very last element of a list?
- How do you reverse a list without using a loop or `.reverse()`?
- How do you add a new element to the end of a list?
- How do you find the total number of elements inside a list?
- Given a list of numbers, how do you find the sum without using a loop?
- How do you find the largest and smallest numbers using built-in functions?
- How do you count how many times the number `5` appears?
- How do you extract a new list containing only the first three elements?
- How do you completely empty a list?
- How do you check if `"Python"` exists inside a list without loops?

### Basic / Intermediate / Advanced (With Loops)

**Basic**

- Print each element on a new line using a for loop.
- Find the sum of all numerical elements using a loop.
- Find the largest number without using `max()`.
- Count how many times a specific element appears using a loop.
- Create a new list containing squares of all numbers from an existing list.

**Intermediate**

- Reverse the elements of a list in-place using a loop.
- Find and print only the even numbers.
- Remove all duplicate values using a loop.
- Check if a specific element exists without using the `in` keyword.

**Advanced**

- Find the second largest number using loops.
- Shift all zeroes to the end while maintaining order (e.g., `[0, 1, 0, 3, 12]` → `[1, 3, 12, 0, 0]`).
- Find common elements between two lists using a nested loop.
- Flatten a nested list using loops.
- Find the frequency of each unique element using loops.

---

## Sets

> File: `15_sets.py`

### With Loops

- Write a program to iterate through a set and print each element multiplied by 10.
- Write a program to find the sum of all numbers in a set using a for loop.
- Given a set of strings, use a loop to count how many elements have length greater than 4.
- Write a program to filter out all odd numbers into a new set using a loop.
- Given a list of sets, combine (union) all of them into a single set using a loop.

### Without Loops

- How do you find the total number of unique elements inside a set?
- Given two sets, how do you find elements common to both?
- How do you add a single element and multiple elements at once?
- Given two sets, how do you get all unique elements from both combined?
- How do you remove an element without raising an error if it doesn't exist?
- How do you check if one set is a completely contained subset of another?
- How do you remove all elements to make a set empty?

---

## Dictionaries

> File: `16_dicts.py`

### With Loops

- Iterate through a dictionary and print all its keys.
- Iterate through a dictionary and print all its values.
- Print both keys and values side-by-side using a loop.
- Given items and prices, calculate total cost of all items using a loop.
- Create a dictionary where keys are 1–5 and values are squares using a `while` loop.
- Filter out items where the value is an even number into a new dictionary.
- Find the key with the highest value using a loop.
- Swap keys and values using a loop.
- Merge two dictionaries manually using a loop.

### Without Loops

- How do you access a value safely without causing a `KeyError`?
- How do you find the total number of key-value pairs?
- How do you add or update a key-value pair?
- How do you remove a key and return its value at the same time?
- How do you check if a key exists without loops?
- How do you clear all items from a dictionary?
- Given two dictionaries, how do you merge them in a single line?
- How do you extract all keys into a list without a loop?
- Given a list of keys, how do you create a dictionary with default value `0` in one step?
- How do you create a shallow copy of a dictionary?

---

## Tuples

> File: `14_tuples.py`

### With Loops

- Iterate through a tuple and print each element on a new line.
- Find the sum of all numerical elements using a for loop.
- Count how many even numbers a tuple contains using a loop.
- Convert a tuple of strings into a single sentence using a loop.
- Check if an element exists without using the `in` keyword.
- Create a new tuple containing only integers from a mixed tuple.
- Find the largest number without using `max()`.
- Copy tuple elements into a list in reverse order using a loop.
- Find the index of a specific element without using `.index()`.
- Given a nested tuple, use nested loops to print every individual number.

### Without Loops

- How do you find the total number of elements inside a tuple?
- How do you find how many times a specific value appears?
- How do you find the index of the first occurrence of an element?
- How do you unpack tuple elements into individual variables?
- How do you reverse a tuple using slicing?
- How do you concatenate two tuples?
- How do you create a tuple that repeats elements 3 times?
- How do you extract a tuple containing only the first three elements?
- How do you check if an item exists in one line?
- Can you change, add, or remove an element after creation? Explain why or why not.

---

## Functions

> File: `18_functions.py`

### Real-Life Scenarios

---
**E-Commerce Price Calculator**

An online store needs a reusable function `calculate_total(price, quantity, discount_percent=0)` that returns the final bill after applying an optional discount. Write the function and show how calling `calculate_total(500, 3, 10)` differs from `calculate_total(500, 3)`.

---
**OTP Generator for Banking App**

A bank sends 6-digit OTPs. Write a function `generate_otp(length=6)` that returns a random numeric string. Why should OTP generation live inside a function instead of being copy-pasted in three different files?

---
**Shipping Cost with *args**

A logistics API receives orders with varying numbers of boxes. Write `total_weight(*weights)` that accepts any number of weight arguments and returns their sum for freight calculation.

Example: `total_weight(2.5, 1.0, 3.2, 0.8)` → `7.5`

---
**User Profile Builder with **kwargs**

A SaaS signup form collects different fields per plan (name, email, company, phone). Write `build_profile(**fields)` that returns a dictionary of all submitted fields. Call it twice with different keyword arguments.

---
**Default Mutable Argument Trap**

A developer writes:

```python
def add_item(item, cart=[]):
    cart.append(item)
    return cart
```

Predict the output of:

```python
print(add_item("apple"))
print(add_item("banana"))
```

Explain the bug and how to fix it for a real shopping-cart feature.

---
**Pure Function vs Side Effect**

Given:

```python
def apply_tax(prices, rate):
    for i in range(len(prices)):
        prices[i] = prices[i] * (1 + rate)
    return prices

data = [100, 200, 300]
result = apply_tax(data, 0.18)
```

Will `data` still be `[100, 200, 300]` after the call? Should a billing function mutate the original list or return a new one?

---
**Lambda for Sorting Job Applicants**

HR has `candidates = [("Anita", 85), ("Ravi", 92), ("Meera", 78)]`. Write a one-liner using `sorted()` and a `lambda` to sort by score descending.

---
**Function as First-Class Object**

You have three payment handlers: `pay_upi`, `pay_card`, `pay_wallet`. Write a function `process_payment(method_func, amount)` that calls whichever payment function is passed in. Why is this pattern useful in real payment gateways?

---
**Scope Bug in Analytics Dashboard**

```python
total = 0

def add_sale(amount):
    total += amount
    return total
```

Why does this crash with `UnboundLocalError`? Fix it for a sales-tracking module using `global` or a better design (return value / class attribute).

---
**Docstring for API Documentation**

Write a function `celsius_to_fahrenheit(c)` with a proper docstring explaining parameters, return value, and an example. Why do teams enforce docstrings before merging code?

---
**Type Hints in a Healthcare API**

Write `calculate_bmi(weight_kg: float, height_m: float) -> float` with validation that raises `ValueError` if height is zero or negative. How do type hints help in large codebases even though Python doesn't enforce them at runtime?

---
**Recursion vs Loop — Folder Size Utility**

You need to calculate total file size in a directory tree. Compare writing this with a loop + stack vs a recursive function. When would you choose recursion for filesystem utilities?

### Without Loops (Function Concepts)

- What is the difference between `return` and `print` inside a function?
- What does `*args` capture when you call `func(1, 2, 3)`?
- What does `**kwargs` capture when you call `func(a=1, b=2)`?
- How do you return multiple values from a single function?
- What is a nested function and where is it used in real projects (e.g., closures)?
- What is the difference between a function defined with `def` and a `lambda`?
- How do you pass a function as an argument to another function?

### Basic / Intermediate / Advanced

**Basic**

- Write a function that checks if a number is even or odd.
- Write a function that returns the area of a rectangle.
- Write a function with a default parameter for currency symbol (`"₹"`).
- Write a function that reverses a string without using slicing.

**Intermediate**

- Write a function that accepts a list and returns only unique elements (preserve order).
- Write a function that validates an Indian mobile number (10 digits, starts with 6–9).
- Write a function decorator-free that times how long another function takes to run (use `time` module).
- Write a function that flattens a list of lists one level deep.

**Advanced**

- Write a function factory `make_multiplier(n)` that returns a function multiplying its input by `n`.
- Write a function using `functools.reduce` to compute product of a list.
- Implement memoization manually for Fibonacci without using `@lru_cache`.
- Write a function that dispatches behavior based on argument type (int vs str vs list).

---

## Generators & Iterators

> File: `20_generators_iterators.py`

### Real-Life Scenarios

---
**Streaming Server Logs (Memory)**

A DevOps tool must read a 10 GB log file line by line. Why is a generator like `read_logs(path)` that `yield`s each line better than `return lines` where `lines = file.readlines()`? What happens to RAM in each approach?

---
**Infinite Twitter / Event Stream**

Design `live_events()` that `yield`s events forever as they arrive. How would you consume only the first 5 events using `next()` without loading the entire stream into memory?

---
**Pagination API Client**

An API returns 100 users per page. Write a generator `fetch_users(pages)` that yields one user at a time across all pages instead of building a giant list. How does this help a dashboard that displays users lazily?

---
**CSV Row Processor**

Given millions of CSV rows, write:

```python
def parse_rows(filepath):
    # yield one dict per row
    ...
```

Why is this preferred over returning `list_of_all_rows` in ETL pipelines?

---
**Pipeline: map + filter as Generator Chain**

You have sensor readings `[12, 45, 0, -3, 88, 102]`. Chain generators to:

1. Ignore invalid (≤ 0) readings
2. Convert Celsius to Fahrenheit
3. Yield only values above 100°F

Write this as a lazy pipeline without storing intermediate full lists.

---
**StopIteration in Production**

```python
def tasks():
    yield "send_email"
    yield "charge_card"
    yield "update_inventory"

workflow = tasks()
```

What happens if a bug calls `next(workflow)` four times? How do `for` loops handle this differently?

---
**Custom Iterator Class — Batch Iterator**

A warehouse scans items in batches of 50. Implement class `BatchIterator` with `__iter__` and `__next__` that yields lists of 50 SKUs from a long list. When is a class-based iterator better than a generator function?

---
**Generator Expression vs List Comprehension**

Compare memory usage of:

```python
squares_list = [x * x for x in range(10_000_000)]
squares_gen = (x * x for x in range(10_000_000))
```

Which one should you pass to `sum()` when processing large datasets and why?

---
**yield from — Delegating Sub-Generators**

A music app merges playlists from multiple sources. Write `merged_playlist(*playlists)` using `yield from` to flatten nested generators. How is this cleaner than nested `for` loops?

---
**Restarting a Generator**

```python
g = count_from(1)
print(next(g))  # 1
print(next(g))  # 2
g = count_from(1)
print(next(g))  # ?
```

Explain why generators are one-pass iterators and how you'd replay data (hint: recreate generator or store in list).

---
**Real-Time Dashboard Throttling**

A dashboard polls CPU metrics every second but UI updates only every 5 seconds. Write a generator that yields every 5th reading from `infinite_metrics()`. Where does this pattern appear in monitoring tools?

---
**Fibonacci Generator for Backtesting**

A trading script needs Fibonacci numbers on demand up to millions. Compare:

```python
def fib_list(n): ...      # returns list
def fib_gen(n): ...       # yields values
```

Which is safer for `n = 1_000_000` and why?

### Iterator Protocol (Conceptual)

- What two methods must an object implement to be an iterator?
- What is the difference between an **iterable** and an **iterator**?
- What exception signals that a generator is exhausted?
- Can you use `len()` on a generator object? Why or why not?
- How does a `for` loop internally call `iter()` and `next()`?

### Basic / Intermediate / Advanced

**Basic**

- Write a generator function that yields numbers from 1 to `n`.
- Write a generator that yields even numbers up to `n`.
- Convert `[1, 2, 3, 4, 5]` into an iterator using `iter()` and print elements with `next()`.
- Write a generator expression that yields squares of numbers 1–10.

**Intermediate**

- Write `read_file_lines(path)` generator that yields stripped non-empty lines.
- Write `windowed(data, size=3)` that yields sliding windows: `(1,2,3), (2,3,4), ...`
- Write a generator that yields prime numbers indefinitely; consume first 10 with a loop.
- Implement `enumerate`-like behavior manually using a generator.

**Advanced**

- Write a coroutine-style generator that receives values via `.send()` (mini pipeline).
- Build a lazy `flat_map(gen, func)` utility.
- Implement `itertools.islice` behavior manually for any iterable.
- Compare performance (memory + time) of list vs generator for a 1M element pipeline.

---

## Decorators

> File: `21_decorators.py`

### Real-Life Scenarios

---
**Login Required — Web Route Protection**

Flask/Django-style pseudocode:

```python
@login_required
def view_profile():
    return "User profile page"
```

Write a `login_required` decorator that checks `current_user.is_authenticated` and redirects to login if false. Why is a decorator better than copying the check into 40 route functions?

---
**Timing Slow Database Queries**

Write `@timing` that prints how long a function took. Apply it to `fetch_orders()` that simulates a slow query. How would this help during performance debugging?

---
**Retry on Network Failure**

An API client calls an unstable payment gateway. Write `@retry(max_attempts=3, delay=1)` that retries on `ConnectionError`. Where is this pattern used in production microservices?

---
**Rate Limiter for Public API**

Write `@rate_limit(calls=5, period=60)` that raises an error if a function is called more than 5 times per minute. Why do public APIs wrap endpoints with rate-limit decorators?

---
**Logging Decorator for Audit Trail**

Banking apps must log every transfer attempt. Write `@audit_log` that logs function name, arguments, timestamp, and return value before and after execution. Why is centralized logging via decorators preferred?

---
**Decorator Stacking Order**

```python
@decorator_a
@decorator_b
def compute():
    ...
```

Which decorator runs first — the one closest to the function or the top one? Predict output if `@uppercase` wraps `@add_exclamation` wraps `def greet(): return "hello"`.

---
**Decorator with Arguments — Role Based Access**

Write `@require_role("admin")` that returns a decorator checking user roles. Usage:

```python
@require_role("admin")
def delete_user(user_id):
    ...
```

Explain the three levels: decorator factory → decorator → wrapper.

---
**Preserve Function Metadata**

After applying `@timing`, why might `help(fetch_orders)` show the wrong name/docstring? Fix it using `functools.wraps`. Why does this matter for debugging and API docs?

---
**Class-Based Decorator**

Implement `class CountCalls` that tracks how many times `process_payment` was invoked. When would you use a class as a decorator instead of a nested function?

---
**Caching Expensive Reports**

Write `@memoize` that stores results of `generate_monthly_report(year, month)` in a dict. Compare this to `functools.lru_cache`. When should cache be cleared in a real app?

---
**Validate Input Before Processing**

Write `@validate_positive` that ensures all numeric arguments are > 0 before calling a loan EMI calculator. How does this separate validation from business logic?

---
**Flask-Style `@app.route("/users")`**

Explain conceptually how a web framework uses decorators to register URLs. You don't need Flask installed — describe what the decorator must do with the function reference.

---
**Debugging Wrapper**

```python
def debug(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper
```

Apply to a function that divides two numbers. What gets printed when `divide(10, 2)` and when `divide(10, 0)`?

---
**Decorator vs Inheritance vs Mixin**

Your team needs auth checks on 15 methods. Compare: base class with auth, mixin class, or decorators. When is each approach cleaner?

---
**Property vs Decorator**

Explain the difference between `@property` on a class method and a standalone function decorator. Give a real example where `@property` exposes a computed `full_name` from `first_name` and `last_name`.

### Conceptual Questions

- What three things happen when Python sees `@decorator` above a function?
- Can a decorator accept arguments? How is `@dec(n=3)` different from `@dec`?
- Can you decorate a generator function? What changes in behavior?
- What is the difference between `@staticmethod` and `@classmethod`?
- How does `@functools.lru_cache` work under the hood at a high level?

### Basic / Intermediate / Advanced

**Basic**

- Write a decorator `@ shout` that prints `"!!!"` before and after a function runs.
- Write a decorator that converts the return value of any function to uppercase (strings only).
- Write a decorator that returns `None` if any exception occurs inside the wrapped function.

**Intermediate**

- Write `@repeat(n)` decorator factory that calls a function `n` times.
- Write a decorator that enforces a maximum of 3 positional arguments.
- Write `@singleton` that ensures a class only creates one instance (class decorator pattern).

**Advanced**

- Write a parametrized caching decorator with TTL (time-to-live in seconds).
- Write a decorator that runs the wrapped function in a separate thread (conceptual — use `threading`).
- Implement a simple `@deprecated` decorator that emits a warning when old API functions are called.
- Build `@typechecked` that validates argument types before function execution.

---

## What to Learn Next (Expert Roadmap)

You already cover fundamentals through intermediate topics (files, OOP, OS, JSON, HTTP). To move toward **expert-level Python**, study these in order:

### Phase 1 — Expert / Production

| Topic | Why |
|-------|-----|
| **Web frameworks** (FastAPI, Django, Flask) | Backend career standard |
| **Databases** (SQLAlchemy, asyncpg, Redis) | Real apps need persistence |
| **Docker & CI/CD** | Deploy what you build |
| **Security** (OWASP, secrets, input sanitization) | Non-negotiable in production |
| **System design with Python** | Queues, workers, event-driven architecture |
| **Open source contribution** | Read CPython source, popular libraries |

### Suggested Practice Projects (Expert Path)

1. **CLI tool** — argparse/typer, config files, logging, pytest
2. **REST API** — FastAPI + SQLAlchemy + JWT auth + Docker
3. **Data pipeline** — scrape → clean (generators) → store → schedule
4. **Async chat server** — websockets + asyncio
5. **Library on PyPI** — typed, tested, documented package

### Current Folder Layout (Sequential)

```
 1_hello.py                  19_recursion.py
 2_variables.py              20_generators_iterators.py
 3_type_convert.py           21_decorators.py
 4_input.py                  22_errorhandle.py
 5_operators.py               23_comprehension.py
 6_ifelse.py                  24_inbuild_functions.py
 7_if_else_practice.py       25_classes.py
 8_matchcase.py              26_class_inheritance.py
 9_while.py                   27_class_practice.py
10_jump_statements.py        28_class_encapsulation.py
11_forloop.py                29_class_operator_overloading.py
12_strings.py                30_bar_mod.py
13_lists.py                  31_osmod.py
14_tuples.py                 32_datetimemod.py
15_sets.py                   33_json.py
16_dicts.py                  34_virtualenv.py
17_file_handling.py         35_requests.py
18_functions.py              QNA.md (this file)
```

Practice / misc files (`prac.py`, `test.py`, `bars.py`, `folder1/`, `folder2/`) are kept separate from the numbered lesson sequence.

---

*Keep adding Q&A sections here as you finish each new lesson file.*
