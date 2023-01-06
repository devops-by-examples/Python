# List Comprehensions

This is definitely the most commonly used on in Python.You'll see them everywhere.

List comprehensions provide us with a simple way to create a list based on some sequence or another list that we can loop over. In python terminology, anything that we can loop over is called iterable. At its most basic level, list comprehension is a syntactic construct for creating lists from existing lists.

List comprehension has these essential parts :

- An iterable input sequence (this could be a list, a range, or any sequence) that we iterate using a variable name.
- An output expression
- An optional condition for the variable to filter or map or do some logical action

Basic syntax is as follows:

```txt
  my_list = [<expression> for <item> in <iterable> if <condition>]
```

Let's have an example for demonstration.Suppose we have a list with just 1-10 integers


```txt
my_list = [1,2,3,4,5,6,7,8,9,10]
```

What we want to do is to create a list named **new_list** with the numbers in the list named **my_list**
- Filter the number to have only even numbers(use **condition**)
- With the filtered number, plus one to it before it is pushed into new list(use **expression**)

```commandline
new_list = [number + 1 for number in my_list if number%2==0]
```

What if we don't use the List comprehension?Below is the example.

```commandline
new_list = []
for number in my_list:
    if number%2 == 0:
        new_list.append(number + 1)
```
