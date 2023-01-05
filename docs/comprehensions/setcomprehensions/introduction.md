##Set Comprehension

Set comprehension is a method for creating sets in python using the elements from other iterables like lists, sets, or tuples. Just like we use list comprehension to create lists, we can use set comprehension instead of for loop to create a new set and add elements to it.

The only difference between a Set Comprehension and a List comprehension is the former uses curly braces **{}** rather than **[]**.

The syntax is as follows:

```commandline
my_set = {<expressio> for <item> in <iterable> if <condition>}
```

The main difference between Set and Dict Comprehension is Set Comprehension doesn't have the **ket:value** pair, but only the **expression**

Lets see how it works with the below example:


```commandline
persons = [
    {
        'name': 'Alice',
        'age': 30,
        'title': 'Data Scientist'
    },
    {
        'name': 'Bob',
        'age': 35,
        'title': 'Data Engineer'
    },
    {
        'name': 'Chris',
        'age': 33,
        'title': 'Machine Learning Engineer'
    }
]

```

Suppose we are not using the set comprehension, the code will be as below:

```commandline
data_employees_set = set()
for p in persons:
    if 'Data' in p['title']:
        data_employees[p['name']] = p['title']

```

If we use it, the code willl be as below:

```commandline
data_employees_set = {p['name'] for p in person if 'Data' in p['title']}
```

Keep in mind that the difference between a Set and a List is that the items in a Set cannot be repeated and not in order.