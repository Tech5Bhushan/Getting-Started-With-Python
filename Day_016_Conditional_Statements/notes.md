# Day 016 - Conditional Statements

Conditional Statements allow Python programs to make decisions.

## if

Executes code when a condition is True.

```python
age = 20

if age >= 18:
    print("Eligible")
```

## if-else

```python
age = 16

if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")
```

## if-elif-else

```python
score = 75

if score >= 80:
    print("Excellent")
elif score >= 60:
    print("Good")
else:
    print("Keep Learning")
```

## Comparison Operators

```text
==    Equal
!=    Not Equal
>     Greater Than
<     Less Than
>=    Greater Than or Equal
<=    Less Than or Equal
```

## Logical Operators

### and

Both conditions must be True.

```python
if age >= 18 and has_license:
    print("Can Drive")
```

### or

At least one condition must be True.

```python
if day == "Saturday" or day == "Sunday":
    print("Weekend")
```

### not

Reverses the condition.

```python
if not is_logged_in:
    print("Please Login")
```

## Important

Assignment:

```python
status = "PASS"
```

Comparison:

```python
status == "PASS"
```

Do not confuse `=` with `==`.

## Key Takeaways

- `if` checks a condition.
- `elif` checks another condition.
- `else` handles the remaining case.
- Conditions evaluate to `True` or `False`.
- `and`, `or`, and `not` combine or modify conditions.
- Python uses indentation to define code blocks.
- Condition order matters.

Learn. Build. Automate. 🚀