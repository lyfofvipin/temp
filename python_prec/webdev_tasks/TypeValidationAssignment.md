# Python Type Validation Assignment

Here without using MYPY try to guess which one are correct as per type validation.

---

### **Part 1: Basic Types & Unions**

1. 
```python
age: int = 25
```

2. 
```python
temperature: int | float = 36.6
```

3. 
```python
status_code: int | None = "200"
```

4. 
```python
user_email: str | None = None
```

---

### **Part 2: Lists & Nested Lists**

5. 
```python
items: list[int] = [1, 2, 3, 4, 5]
```

6. 
```python
names: list[str] = ["Alice", "Bob", 101]
```

7. 
```python
grid: list[list[int]] = [[1, 2, 3], [4, 5, 6]]
```

8. 
```python
ragged_grid: list[list[int]] = [[1, 2], [3, "4"]]
```

---

### **Part 3: Dictionaries & Sets**

9. 
```python
user_roles: dict[str, str] = {"alice": "admin", "bob": "user"}
```

10. 
```python
permissions: dict[str, set[str]] = {
    "admin": {"read", "write"},
    "guest": {"read"}
}
```

11. 
```python
config: dict[str, int | bool] = {"timeout": 30, "debug": True}
```

12. 
```python
invalid_dict: dict[str, int] = {100: "score", 200: "bonus"}
```

---

### **Part 4: Fixed-Length Tuples**

13. 
```python
coordinates: tuple[float, float] = (34.0522, -118.2437)
```

14. 
```python
employee: tuple[str, int, float] = ("Jane Doe", 30, 75000.50)
```

15. 
```python
bad_employee: tuple[str, int, float] = ("John Doe", "thirty", 65000.0)
```

16. 
```python
short_point: tuple[float, float, str] = (37.7749, -122.4194)
```

---

### **Part 5: Variable-Length & Ellipsis Tuples**

17. 
```python
exam_scores: tuple[int, ...] = (85, 90, 78, 92)
```

18. 
```python
mixed_scores: tuple[int, ...] = (90, 85.5, 88)
```

19. 
```python
empty_scores: tuple[int, ...] = ()
```

20. 
```python
profile: tuple[str, int, ...] = ("Alice", 25, "Developer", "New York")
```
