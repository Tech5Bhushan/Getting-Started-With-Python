# Day 010 - String Methods

Python provides several built-in methods for working with strings.

## upper()

Converts characters to uppercase.

```python
name = "Bhushan"
print(name.upper())
```

Output:

```text
BHUSHAN
```

## lower()

Converts characters to lowercase.

```python
name = "BHUSHAN"
print(name.lower())
```

## title()

Converts the first character of each word to uppercase.

```python
text = "getting started with python"
print(text.title())
```

## strip()

Removes leading and trailing whitespace.

```python
text = "   Python   "
print(text.strip())
```

## replace()

Replaces text.

```python
text = "I am learning Java"
print(text.replace("Java", "Python"))
```

## split()

Splits a string and returns a list.

```python
languages = "Python,Java,C++"
print(languages.split(","))
```

## find()

Returns the index of the first occurrence.

```python
text = "Learning Python"
print(text.find("Python"))
```

Output:

```text
9
```

## count()

Counts occurrences.

```python
text = "banana"
print(text.count("a"))
```

Output:

```text
3
```

## Method Chaining

Methods can also be combined.

```python
name = "   bhushan more   "

print(name.strip().title())
```

Output:

```text
Bhushan More
```

## Key Takeaways

- `upper()` → Uppercase
- `lower()` → Lowercase
- `title()` → Title Case
- `strip()` → Remove surrounding whitespace
- `replace()` → Replace text
- `split()` → Split a string
- `find()` → Find position
- `count()` → Count occurrences

Learn. Build. Automate. 🚀