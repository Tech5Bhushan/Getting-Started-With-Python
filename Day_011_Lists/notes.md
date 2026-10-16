# Day 011 - Lists in Python

A List is used to store multiple values in a single variable.

## Creating a List

```python
languages = ["Python", "Java", "C++"]
```

## Accessing Elements

Python List indexing starts from 0.

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

## Changing Elements

Lists are mutable.

```python
languages[1] = "JavaScript"

print(languages)
```

Output:

```text
['Python', 'JavaScript', 'C++']
```

## List Length

Use `len()` to find the number of elements.

```python
print(len(languages))
```

Output:

```text
3
```

## Mixed Data Types

Lists can contain different types of data.

```python
person = ["Bhushan", 34, 5.9, True]
```

## Duplicate Values

Lists can contain duplicates.

```python
skills = ["Python", "CANoe", "Python"]
```

## Key Takeaways

- Lists store multiple values.
- Lists use square brackets `[]`.
- Indexing starts from `0`.
- Negative indexing starts from the end.
- Lists are mutable.
- Lists allow duplicate values.
- Lists can store different data types.
- `len()` returns the number of elements.

Learn. Build. Automate. 🚀