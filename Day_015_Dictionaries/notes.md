# Day 015 - Dictionaries in Python

A Dictionary stores information as key-value pairs.

## Creating a Dictionary

```python
person = {
    "name": "Bhushan",
    "city": "Bengaluru",
    "skill": "Python"
}
```

## Accessing Values

```python
print(person["name"])
```

Output:

```text
Bhushan
```

## Using get()

```python
print(person.get("city"))
```

A default value can also be provided:

```python
print(person.get("company", "Not Available"))
```

## Adding an Entry

```python
person["experience"] = 8
```

## Updating an Entry

```python
person["skill"] = "Python Automation"
```

## Removing an Entry

```python
person.pop("city")
```

## Dictionary Methods

### keys()

```python
person.keys()
```

Returns the keys.

### values()

```python
person.values()
```

Returns the values.

### items()

```python
person.items()
```

Returns key-value pairs.

## Nested Data

A Dictionary value can contain another collection.

```python
engineer = {
    "name": "Bhushan",
    "skills": ["Python", "CANoe", "UDS"]
}
```

## Key Characteristics

- Stores key-value pairs
- Mutable
- Keys must be unique
- Values can use different data types
- Values can contain other collections
- Access values using keys

## Key Takeaways

- `{}` creates a Dictionary when used with key-value pairs.
- `dictionary[key]` accesses a value.
- `get()` can safely retrieve potentially missing keys.
- Assignment can add or update entries.
- `pop()` removes an entry.
- `keys()` provides keys.
- `values()` provides values.
- `items()` provides key-value pairs.

Learn. Build. Automate. 🚀