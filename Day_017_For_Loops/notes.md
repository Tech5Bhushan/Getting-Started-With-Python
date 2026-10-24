# Day 017 - for Loops in Python

A `for` loop is used to iterate through an iterable and repeatedly execute code.

## Basic Syntax

```python
for item in collection:
    print(item)
```

## Loop Through a List

```python
languages = ["Python", "Java", "C++"]

for language in languages:
    print(language)
```

## range()

### range(stop)

```python
for number in range(5):
    print(number)
```

Output:

```text
0
1
2
3
4
```

The stop value is excluded.

### range(start, stop)

```python
for number in range(1, 6):
    print(number)
```

### range(start, stop, step)

```python
for number in range(0, 10, 2):
    print(number)
```

Output:

```text
0
2
4
6
8
```

## Loop Through a String

```python
for character in "Python":
    print(character)
```

## Loop Through a Dictionary

```python
test_result = {
    "test_id": "TC_101",
    "status": "PASS"
}

for key, value in test_result.items():
    print(key, value)
```

## Loop with a Condition

```python
for number in range(1, 6):

    if number % 2 == 0:
        print(number)
```

## Nested Loop

```python
for row in range(3):

    for column in range(2):
        print(row, column)
```

## Key Takeaways

- `for` loops repeat operations.
- Lists, Tuples, Sets, Strings, Dictionaries, and other iterables can be traversed.
- `range()` is useful for numeric iteration.
- The stop value of `range()` is excluded.
- `range()` supports `start`, `stop`, and `step`.
- Loops can contain conditions.
- Loops can be nested.
- Set iteration order should not be relied upon.
- Meaningful loop-variable names improve readability.

Learn. Build. Automate. 🚀