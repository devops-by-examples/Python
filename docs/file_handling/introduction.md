# File Handling

File handling has always been vital to a huge part of development community.But, why?

Take a minute and think about this situation — You have a server up and running and you need to access files present on that server. You can do this remotely, or you need to work with files locally by giving some input to your python program on the server or so

So how can we input something to Python?

- **Standard input** - The usual keyboard input
- **Command Line arguments** - To input some parameter into the code while executing

But, think of this situation too - What if you had to read lots of data which is not practical to type in every single time?

So, what is the easiest way out here to store whatever input you want in one place and keep using it as long as it is required can be achieved using Files!

**Types of files supported in Python**

Python supports mainly two types of files:

- Binary
- Text

A binary file is any type of file that is not a text file. Because of their nature, binary files can only be processed by an application that knows or understand the file’s structure. In other words, they must be applications that can read and interpret binary.

Text files are structured as a sequence of lines, where each line includes a sequence of characters. This is what you know as code or syntax. Each line is terminated with a special character, called the EOL or End of Line character.

### File Operations:

The main operation sin files are called **CRUD**

- Create
- Read
- Update
- Delete

However, do note that there are many other operations that can be performed with the files as well.Such as, copying a file or changing the properties of the file.

Basic steps are 

```commandline
Create File -> Open File-> Perform actions -> Close File
```
Creation of file can be done manually or through Python. For now, let us consider that we will do it manually by going to the location and creating a file like a text file.

### open() function in Python:

Now we will check out how we can open a file in Python. It is very simple — we have an inbuilt function called the open function which is used for this exact purpose. The open function takes in 2 parameters — one is the filename and the other is the mode.

Syntax for the open function is as below:

```commandline
file_object  = open(“filename”, “mode”) 
```
### Open Modes:

These are the various modes available to open a file. We can open in read mode, write mode, append mode and create mode as well. Pretty straightforward. But do note that the default mode is the read mode.

Including a mode argument is optional because a default value of ‘r’ will be assumed if it is omitted. The ‘r’ value stands for read mode, which is just one of many.

The modes are:

‘r’ — Read mode which is used when the file is only being read
‘w’ — Write mode which is used to edit and write new information to the file (any existing files with the same name will be erased when this mode is activated)
‘a’ — Appending mode, which is used to add new data to the end of the file; that is new information is automatically amended to the end
‘r+’ — Special read and write mode, which is used to handle both actions when working with a file

### Creating A Text File Using Python
To get more familiar with text files in Python, what’s better than beginning by creating our own. We will check out some examples as well!

Using any simple text editor of your choice, let’s create a file first. You can name it anything you like at this point, and it’s better to use something you’ll identify with.

For the purpose of this tutorial, however, we are going to call it “demofile.txt”. Just create the file and leave it blank.

Check out the following code, you could copy the same thing and post it over into your editor as well!

```
file = open(“demofile.txt”,”w”) 
file.write(“Hello World”) 
file.write(“Welcome to Python Class”) 
file.write(“Today's class is about files”) 
file.close()
```

**Output**

$ cat demo.txt 
```
Hello World 
Welcome to Python Class
Today's class is about files
```
Next, let us look at how we can read a text file using Python.

### Reading a Text file in Python

There are so many ways in which you can read a text file in Python. But, let us start with the simple stuff and work on from there.

If you need to extract a string that contains all the characters in the file, you can use the following method:

```
file.read()
```
The full code to work with this method will look something like this:
```commandline
file = open(“demo.txt”, “r”)  
print file.read()
```

Here are so many ways in which you can read a text file in Python. But, let us start with the simple stuff and work on from there.

If you need to extract a string that contains all the characters in the file, you can use the following method:

```
file.read()
```
The full code to work with this method will look something like this:

```commandline
file = open(“demo.txt”, “r”)  
print file.read()
```
The output of that command will display all the text inside the file.

For example, with the following code the interpreter will read the first five characters of stored data and return it as a string:

```
file = open(“demo.txt”, “r”)   
print file.read(5)
```

The output for this will look like:

```commandline
Hello
```
Each time you run the method, it will return a string of characters that contains a single line of information from the file.

```
file = open(“demo.txt”, “r”)  
print file.readline():
```
This would return the first line of the file:

```
Hello World
```
If we wanted to return only the third line in the file, we would use this:

```
file = open(“testfile.txt”, “r”)  
print file.readline(3):
```

But what if we wanted to return every line in the file, properly separated? You would use the file.readlines() function.

```commandline
file = open(“testfile.txt”, “r”)  
print file.readlines()
```

Output from this is:
```commandline
[‘Hello World’, ‘Welcome to Python Class’, ‘Today's class is about files’]
```

### Looping over a File Object in Python

When you want to read — or return — all the lines from a file in a more memory efficient way you can use the below method:
```commandline
file = open(“demo.txt”, “r”)  
for line in file:  
print line
```

This will return:

```
Hello World 
Welcome to Python Class
Today's class is about files
```

### File Write Method In Python
One thing you’ll notice about the file write method is that it only requires a single parameter, which is the string you want to write.

This method is used to add information or content to an existing file. To start a new line after you write data to the file, you can add an EOL character.

```
file = open(“demofile.txt”, “w”)
file.write(“This is a test”) 
file.write(“To add more lines.”)
file.close()
```
Obviously, this will amend our current file to include the two new lines of text.



### Closing A File In Python
When you’re done working, you can use the fh.close() command to end things. What this does is close the file completely, terminating resources in use, in turn freeing them up for the system to deploy elsewhere.

### Splitting Lines In A Text File
As a final example, let’s explore a unique function that allows you to split the lines taken from a text file.

But just because we are going to use it to split lines after a space character, doesn’t mean that’s the only way. You can actually split your text using any character you wish — such as a colon, for instance.

The code to do this (also using a with statement) is

```
with open(“hello.text”, “r”) as f:
data = f.readlines()
  
for line in data:
words = line.split()
print words
```
If you wanted to use a colon instead of a space to split your text, you would simply change line.split() to line.split(“:”).

The output for this will be:
```commandline
[“hello”, “world”, “how”, “are”, “you”, “today?”]
```

