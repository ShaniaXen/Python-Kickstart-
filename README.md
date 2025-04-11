# Python List Construction Methods

This section compares two common methods to build lists in Python:

---

## ✅ Traditional Method Using `append()`

This is the step-by-step approach where we:

1. Start with an empty list.
2. Use a loop to compute values.
3. Use the `.append()` method to collect results.

```python
squares = []
for x in range(1, 11):
    squares.append(x**2)

print(squares)

Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

##What is List Comprehension?LIST COMPREHENSION IS THE MODERN PYTHONIC WAY OF WRITING LOGIC INSIDE LIST

List comprehension is a concise way to create lists in Python. It combines the for loop, an expression, and optional condition into a single line of code.

### Nested List Comprehension

Basic Syntax               [expression for item in iterable]
With Condition Logic       [expression for item in iterable if condition]
Nested List Comprehension  [expression for item1 in iterable1 for item2 in iterable2]
[[expression for inner in inner_loop] for outer in outer_loop]

BASIC SYNTAX:
[expression for item in iterable]
Generate Squares of Numbers Using List Comprehension
# This one-liner generates squares of numbers from 0 to 9 using list comprehension
squares = [x**2 for x in range(10)]

print("Squares using list comprehension:")
print(squares)

OUTPUT: Squares using list comprehension:
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
