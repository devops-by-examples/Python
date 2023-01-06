# Dictionary Comprehensions

The name **"Something"** Comprehension, is actually depending on the output object type rather than the iterable that is used in the comprehension.Therefore, a Dictionary Comprehension will generate a Dictionary.

The basic syntax is ad follows:

```commandline
my_dict = {<key>:<value> for <item> in <iterable> if <condition>}
```

Please be noticed that the **key** and the **value** here can be expressions with or without **item**.

Let’s say that we have a list of dictionary objects which contain employee names, age and job titles.

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

The requirement is to get all the employees having their title contains the string “Data”. So, we can call them “data employees”.

Also, we’re not interested in the employees’ age, so that we want to have such a dictionary with the employee names as the keys and their job titles as the value.

```commandline
data_employees = {}
for p in persons:
    if 'Data' in p['title']:
        data_employees[p['name']] = p['title']
```

Again, we have to initialise an empty dictionary at the beginning. Inside the for-loop, we will put the if-condition to filter the employees’ job title. Finally, we need to make sure that the structure of the new dictionary obeys the requirements.

With Dictionary Comprehension, we can put all these in one line and even in prove its readability.

```commandline
data_employees = {p['name']:p['title'] for p in persons if 'Data' in p['title']}
```

Besides concise, I would say that the Dictionary Comprehension is even more readable.