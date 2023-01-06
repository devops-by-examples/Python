Last but not the least, Generator Comprehension is also not known by most of the people. The generator is a quite unique syntax in Python, it is usually generated from a function with yield keyword rather than Python.

For example, let’s use the same number list and requirements from the List Comprehension section. We can define a function to make a generator for us.

```commandline
def even_generator(numbers):
    for n in numbers:
        if n % 2 == 0:
            yield int(n/2)
eg = even_generator(my_list)
```

A generator can be iterated by its built-in function ```next()```.So, we can keep getting the next value of the generator by calling ```print(next(eg))```

In fact, all these can be done using Generator Comprehension. The only difference between Generator Comprehension and List Comprehension is that the former uses parentheses.


```commandline
my_gen = (<expression> for <item> in <iterable> if <condition>)
```

Yes, we even don’t need the yield keyword! Let’s give it a try.

```commandline
eg = (int(number/2) for number in my_list if number % 2 == 0)
```