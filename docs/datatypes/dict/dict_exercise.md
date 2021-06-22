# Questions on Dicts

## Question 1

Concatenate the below dictionaries to create a new one.

Example:

```txt
dic1={10:100, 20:200}
dic2={30:300, 40:400}
dic3={50:500, 60:600}
```

Expected Output:

```txt
{10: 100, 20: 200, 30: 300, 40: 400, 50: 500, 60: 600}
```
```python
dic4 = {}
for d in (dic1, dic2, dic3): 
    dic4.update(d)
    print(dic4)
```

## Question 2

print a dictionary that takes input as n and print the dict in the form (n, n*n*n). 

Example:

```txt
n = 3
```

Expected Output:

```txt
{1: 1, 2: 8, 3: 27}
```
```python
n=int(input("Input a number "))
d = dict()

for x in range(1,n+1):
    d[x]=x*x*x

print(d)
```

## Question 3

Program to sort a given dictionary by key

dict1 = {'a': 10, 'z': 30, 'f': 20}

Expected Output:

```txt
a: 10
f: 20
z: 30

```
```python
for key in sorted(dict1):
    print("%s: %s" % (key, dict1[key]))
```

## Question 4
Create a dictionary from the given string with the letters count as value in it.

Example:

```txt
string1='aabbcccd'
```

Expected Output:

```txt
{'a': 2,'b': 2, 'c': 3,'d':1} 
```

