# Dictionaries 

A dictionary consists of a collection of key-value pairs. Each key-value pair maps the key to its associated value.

```txt
dict = {
    <key>: <value>,
    <key>: <value>,
      .
      .
      .
    <key>: <value>
}
```

Dictionaries and lists share the following characteristics:

* Both are mutable.
* Both are dynamic. They can grow and shrink as needed.
* Both can be nested. A list can contain another list. A dictionary can contain another dictionary. A dictionary can also contain a list, and vice versa.

Dictionaries differ from lists primarily in how elements are accessed:

* List elements are accessed by their position in the list, via indexing.
* Dictionary elements are accessed via keys.

## Accessing Dictionary Values

A value is retrieved from a dictionary by specifying its corresponding key in square brackets.

```python
car = dict( colour = 'Black', brand = "Ford", model = "Mustang", year = 2021)
print(car)
print car['colour']
print car['brand]
```

Output:

```txt
{'colour': 'Black', 'brand': 'Ford', 'model': 'Mustang', 'year': 2021}
'Black'
'Ford'
```

## Add an entry

Adding an entry to an existing dictionary is simply a matter of assigning a new key and value.

```python
car['city'] = 'Hyderabad'
car
```

Output:

```txt
{'colour': 'Black', 'brand': 'Ford', 'model': 'Mustang', 'year': 2021, 'city': 'Hyderabad'}
```

## Update an entry

To update an entry, you can just assign a new value to an existing key.

```python
car['city'] = 'Banglore'
car
```

Output:

```txt
{'colour': 'Black', 'brand': 'Ford', 'model': 'Mustang', 'year': 2021, 'city': 'Banglore'}
```

## Delete an entry

To delete an entry, use the del statement, specifying the key to delete.

```python
del car['brand']
car
```

Output:

```txt
{'colour': 'Black', 'model': 'Mustang', 'year': 2021, 'city': 'Banglore'}
```




