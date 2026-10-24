# Day 018 - while Loops in Python

A `while` loop repeatedly executes code while a condition remains `True`.

## Basic Syntax

```python
while condition:
    code_to_execute
```

## Basic Example

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

Output:

```text
1
2
3
4
5
```

## Infinite Loop

```python
while True:
    print("Running")
```

This continues indefinitely unless the loop is interrupted or an exit condition is introduced.

## break

`break` exits the current loop.

```python
count = 1

while True:

    print(count)

    if count == 5:
        break

    count += 1
```

## continue

`continue` skips the remaining code in the current iteration.

```python
number = 0

while number < 5:

    number += 1

    if number == 3:
        continue

    print(number)
```

Output:

```text
1
2
4
5
```

## for vs while

Use `for` when iterating through an iterable or defined range.

```python
for number in range(5):
    print(number)
```

Use `while` when repetition depends on a condition.

```python
while condition:
    do_something()
```

## Common Uses

- Retry logic
- Input validation
- Waiting for a condition
- Repeated status checks
- Menu-driven programs

## Key Takeaways

- `while` runs while its condition remains `True`.
- The condition should normally have a path toward becoming `False`.
- `break` exits the loop.
- `continue` skips the current iteration.
- Counters can limit repetitions.
- Infinite loops require careful control.
- `while` loops are useful for retry-based automation.

Learn. Build. Automate. 🚀