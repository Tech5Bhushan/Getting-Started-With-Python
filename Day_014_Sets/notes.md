# Day 014 - Sets in Python

A Set stores unique values.

Sets are unordered, mutable, and not indexed.

## Creating a Set

```python
languages = {"Python", "Java", "C++"}
```

## Duplicate Values

```python
skills = {"Python", "CANoe", "Python"}
```

The Set stores `"Python"` only once.

## Empty Set

Use `set()`:

```python
empty_set = set()
```

Using `{}` creates an empty Dictionary, not an empty Set.

## Adding Elements

### add()

```python
languages.add("JavaScript")
```

### update()

```python
languages.update(["C#", "Go"])
```

## Removing Elements

### remove()

```python
languages.remove("Java")
```

Raises `KeyError` if the value does not exist.

### discard()

```python
languages.discard("Java")
```

Does not raise an error if the value does not exist.

### clear()

```python
languages.clear()
```

## Membership Testing

```python
print("Python" in languages)
```

## Set Operations

### Union

```python
result = set_a.union(set_b)
```

Or:

```python
result = set_a | set_b
```

### Intersection

```python
result = set_a.intersection(set_b)
```

Or:

```python
result = set_a & set_b
```

### Difference

```python
result = set_a.difference(set_b)
```

Or:

```python
result = set_a - set_b
```

### Symmetric Difference

```python
result = set_a.symmetric_difference(set_b)
```

Or:

```python
result = set_a ^ set_b
```

## Removing Duplicates

```python
values = ["Python", "CANoe", "Python"]

unique_values = set(values)
```

## Key Takeaways

- Sets store unique values.
- Sets are unordered.
- Sets are mutable.
- Sets are not indexed.
- `add()` adds one element.
- `update()` adds multiple elements.
- `remove()` can raise `KeyError`.
- `discard()` safely handles missing values.
- `union()` combines unique values.
- `intersection()` finds common values.
- `difference()` finds values exclusive to the first Set.
- `symmetric_difference()` excludes common values.

Learn. Build. Automate. 🚀