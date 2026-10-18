# Day 013 - Tuples in Python

A Tuple is an ordered collection of values.

Tuples are immutable, meaning their elements cannot be reassigned after creation.

## Creating a Tuple

```python
languages = ("Python", "Java", "C++")
```

## Accessing Elements

```python
print(languages[0])
```

Output:

```text
Python
```

## Negative Indexing

```python
print(languages[-1])
```

Output:

```text
C++
```

## Tuple Slicing

```python
languages = ("Python", "Java", "C++", "JavaScript")

print(languages[1:3])
```

Output:

```text
('Java', 'C++')
```

## Tuple Immutability

Tuples cannot be modified by assigning a new value to an element.

```python
languages[1] = "JavaScript"
```

This results in a `TypeError`.

## Single-Element Tuple

A comma is required.

```python
language = ("Python",)
```

Without the comma:

```python
language = ("Python")
```

Python treats it as a string.

## Tuple Packing

```python
vehicle = ("BMW", "X5", 2026)
```

## Tuple Unpacking

```python
brand, model, year = vehicle
```

## count()

```python
skills = ("Python", "CANoe", "Python")

print(skills.count("Python"))
```

Output:

```text
2
```

## index()

```python
tools = ("CANoe", "PyCharm", "GitHub")

print(tools.index("PyCharm"))
```

Output:

```text
1
```

## List vs Tuple

List:

```python
["Python", "Java"]
```

- Mutable
- Uses `[]`

Tuple:

```python
("Python", "Java")
```

- Immutable
- Commonly written using `()`

## Key Takeaways

- Tuples store multiple values.
- Tuples are ordered.
- Tuples are indexed.
- Tuples allow duplicates.
- Tuples can contain mixed data types.
- Tuples are immutable.
- Single-element Tuples require a comma.
- Tuples support packing and unpacking.
- `count()` counts occurrences.
- `index()` finds the first matching position.

Learn. Build. Automate. 🚀