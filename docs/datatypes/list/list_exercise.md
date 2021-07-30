# Questions on Lists

## Question 1

Concatenate two lists index-wise.

Example:

```txt
list1 = ["M", "ho", "to", "i", "war"]
list2 = ["y", "me", "wn", "s", "angal"]
```

Expected Output:

```txt
['My', 'hometown', 'is', 'warangal']
```

## Question 2

Concatenate two lists in the following order.

Example:

```txt
list1 = ["Hi ", "Hey "]
list2 = ["Madam", "Sir"]
```

Expected Output:

```txt
['Hi Madam', 'Hi Sir', 'Hey Madam', 'Hi Sir']
```

## Question 3

Add item 10 after 5 in the following Python List.

sample_list = [1, 2, 5, 6, 7, 9]

## Question 4

Write a program to find the largest element in a list. Similarly, Write a program to find the smallest element in a list.

## Question 5

a = [(111, "a@gmail.com,b@gmail.com"),
     (222, "s@gmail.com,a@gmail.com"),
     (333, 444, "a@gmail.com,b@gmail.com,c@gmail.com")]

This is a list of tuples, Print the unique Gmail IDs

Expected Output:

```txt
{'a@gmail.com', 'b@gmail.com', 's@gmail.com', 'c@gmail.com'}
```

Solution:

```python
a = [(111, "a@gmail.com,b@gmail.com"),
     (222, "s@gmail.com,a@gmail.com"),
     (333, 444, "a@gmail.com,b@gmail.com,c@gmail.com")]
l = []
for i in a:
    for j in i:
       if "gmail.com" in str(j):
           a = j.split(",")
           l.extend(a)

print(set(l))
```
