# For loop

Use a `for` loop when you know how many times the loop should run.

A `for` loop is used for iterating over a sequence data types such as list, tuple, string or dictionary. If you are confused on why is a string considered as sequence? it is because a string is also a character array.

```python
weekdays = ["monday", "tuesday", "wednesday", "thurday", "friday"]
for w in weekdays:
  print(w)
```

Yeah, you guessed the output right.

```txt
monday
tuesday
wednesday
thursday
friday
```

## Conditions

In the above weekdays list, print only when weekday is Wednesday.

```python
weekdays = ["monday", "tuesday", "wednesday", "thurday", "friday"]
for w in weekdays:
    if w == "wednesday":
        print(w)
```

## Break

A `break` statement can be used to control the loop iterations. In a nutshell, `break` breaks the loop execution when a condition is matched.

```python
weekdays = ["monday", "tuesday", "wednesday", "thurday", "friday"]
for w in weekdays:
    print(w)
    if w == "wednesday":
        break
```

Can you guess the output?

Yeah, the output is:

```txt
monday
tuesday
wednesday
```

Let me bring the print statement in the above example after the if condition.

```python
weekdays = ["monday", "tuesday", "wednesday", "thurday", "friday"]
for w in weekdays:
    if w == "wednesday":
        break
    print(w)
```

Can you guess the output now? give it a try.

## continue

A `continue` statement can be used to skip an Iteration of a loop. In a nutshell, `continue` skips the current iteration and moves to the next iteration.

```python
weekdays = ["monday", "tuesday", "wednesday", "thurday", "friday"]
for w in weekdays:
    if w == "wednesday":
        continue
    print(w)
```

output:

```txt
monday
tuesday
thursday
friday
```
