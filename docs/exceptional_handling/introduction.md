## Exceptional Handling

Exception Handling in Python which can be achieved using the “try-except” statement. Exceptions are the events that are triggered when the program encounters an error during execution. When an error occurs, we can handle these exceptions to avoid the program from getting crashed.


In this article, we are going to discuss the following:

- Handling Error using “try-except” block
- Working with Finally Block
- Raising Custom Exceptions


***Why do we Require Exception Handling?***

- In the case of Errors during runtime, the application might terminate unconditionally. Using the Exception Handling, we can handle the scenario of Failures and avoid termination of the program.

***Handling Error using “try-except” block***

Next, we will look into the implementation of simple “try-except” block

```
def implementDivision(a, b):
  value = a/b
  print(value)

implementDivision(10, 0)

```
In the code above, it can be observed that we are trying to divide a number with zero, so we are getting a “ZeroDivisionError” and the program terminates without further processing. Often we require to inform the user about the problem before we terminate the program. In order to handle this situation and to avoid termination of the program, we can use the “try-except” block. We are going to implement the same program using the “try-except” block to see the difference.

```
def implementDivision(a, b):
  try:
    value = a/b
    print(value)
  except FileNotFoundError:
    print("The File Cannot be Found")
  except ZeroDivisionError:
    print("Number Cannot be Divided by Zero")
  except:
    print("This is the Generic Error")

implementDivision(10, 0)

```
In the above code, we have the following benefits:

- Even when we encountered the error during execution, we can see that the program did not terminate immediately. We were able to execute further even after the runtime error since it has been handled.

- We can provide information about the error to the user using the “except” block. Any execution error encountered in the try block is handled inside the corresponding “except” block

***Working with Finally Block in “try-except”***

Finally, Block contains all the execution statements that must be executed whether the exception occurred or not during the program execution. The statement inside “finally” will execute irrespective of failure or success. Let's understand this with the help of a scenario.

Below is the example with try-except and finally block

```

def readFileContent():
  fileReader = None
  try:
    fileReader = open("a.json")
    print(fileReader.read())
  except:
    print("Cannot Read the specified File")
  finally:
    print("Closing File Reader...")
    fileReader.close()

readFileContent()

```

***Raising Custom Exceptions***

In certain scenarios, we need to execute the custom logic to terminate the execution with the custom error or exception. We can trigger the termination with a custom exception that can be handled by the “try-except” block.

Let's create a small function that expects the value between 0 to 100, if the value received by the function is not between the specified range, we can terminate the program with the custom exception.

```
def mainFunction(range):
    try:
      if range > 100 or range < 0:
        raise Exception()
      if range < 100 and range > 0:
        range = range / 2
        range = range + 10
        print(f"The Output for the execution is: {range}")
    except:
        print(f"Number({range}) is not under the specified Range")

mainFunction(150)

```

In the above code, we can see that if the value does not lie with the specified range (0 to 100), we are sending an exception which is then handled by the “except” block. Here we are sending Custom Exceptions and triggering the event for failure/termination. This event is then handled by the “except” block specified. This way we are able to raise Custom Exceptions in our code.

