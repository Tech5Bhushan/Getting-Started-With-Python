# Day 012 - List Methods

Python provides built-in methods for adding, removing, searching, arranging, and copying List elements.

## Adding Elements

### append()

Adds one element to the end.

```python
languages = ["Python", "Java"]
languages.append("C++")
```

### extend()

Adds multiple elements.

```python
languages.extend(["JavaScript", "C#"])
```

### insert()

Adds an element at a specified index.

```python
languages.insert(1, "Go")
```

## Removing Elements

### remove()

Removes the first matching value.

```python
languages.remove("Java")
```

### pop()

Removes and returns an element.

```python
removed_value = languages.pop(1)
```

Without an index, `pop()` removes the final element.

### clear()

Removes every element.

```python
languages.clear()
```

## Searching Elements

### index()

Returns the index of the first matching value.

```python
languages.index("Python")
```

### count()

Returns the number of occurrences.

```python
skills = ["Python", "CANoe", "Python"]
print(skills.count("Python"))
```

## Arranging Elements

### sort()

Arranges the original List.

```python
numbers = [30, 10, 20]
numbers.sort()
```

### reverse()

Reverses the current order.

```python
numbers.reverse()
```

## Copying a List

### copy()

Creates a shallow copy.

```python
original = ["Python", "CANoe"]
copied = original.copy()
```

## Key Takeaways

- `append()` adds one element.
- `extend()` adds multiple elements.
- `insert()` adds at a specified index.
- `remove()` removes by value.
- `pop()` removes by index.
- `clear()` removes all elements.
- `index()` returns the position of a value.
- `count()` counts matching values.
- `sort()` arranges the original List.
- `reverse()` reverses the existing order.
- `copy()` creates a shallow copy.

Learn. Build. Automate. 🚀