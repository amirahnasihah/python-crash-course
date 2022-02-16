<h2>
  Chapter 8: functions
</h2>

<p>
  Learn to write functions, which are named blocks of code that are designed to do one specific job. When you want to perform a particular task that you’ve defined in a function, you call the function responsible for it. If you need to perform that task multiple times throughout your program, you don’t need to type all the code for the same task again and again; you just call the function dedicated to handling that task, and the call tells Python to run the code inside the function. You’ll find that using functions makes your programs easier to write, read, test, and fix. 
<div>
Learn ways to pass information to functions. Learn how to write certain functions whose primary job is to display information and other functions designed to process data and return a value or set of values. Finally, learn to store functions in separate files called modules to help organize your main program files.
</div>
</p>


# functions

- functions are blocks of code that are designed to do one specific job.
- if need perform task multiple times, call the function dedicated to handling that task.

**Learn:**

- ways to pass information to functions.
- store functions in separate files called *modules* to help organize main program files.

## Defining a Function

```python
def greet_user():   #1
    """Display a simple greeting."""    #2
    print("Hello!")     #3

greet_user()    #4
```

- at 1, keyword `def` to inform defining a function. This is the function definition, which tells Python the name of the function and, if applicable, what kind of information the function needs to do its job.
- Parentheses are required to hold that information.
- `greet_user()` needs no information to do its job, so its parentheses are empty.
- Any indented lines that follow `def greet_user()`: make up the body of the function.
- at 2, text is a comment called a *docstring*, which describes what the function does.
- at 3, line `print("Hello!")` is the only line of actual code in the body of this function, so `greet_user()` has just one job: `print("Hello!")`.
- at 4, *function call* execute the code in the function. To *call* a function, write the name of the function, followed by any necessary information in parentheses.

Output:

```python
Hello!
```

### Passing Information to a Function

- the function `greet_user()` can not only tell the user `Hello!` but also greet them by name.
- enter `username` in the parentheses of the function’s definition at `def greet_user()`. By adding `username`, allow the function to accept any value of `username` specify.

```python
def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")
    print(i)
greet_user('jesse')
```

Output:

```python
Hello, Jesse!
```

### Arguments and Parameters

- defined `greet_user()` to require a value for the variable `username`.
- Once called the function and gave it the information (a person’s name), it printed the right greeting.
- variable `username` in the definition of `greet_user()` is an example of a *parameter*, a piece of information the function needs to do its job.
- The value `'jesse'` in `greet_user('jesse')` is an example of an *argument*. An *argument* is a piece of information that’s passed from a function call to a function.
- When call the function, we place the value we want the function to work with in parentheses. In this case the argument `'jesse'` was passed to the function `greet_user()`, and the value was assigned to the parameter `username`.

## Passing Arguments

- a function definition can have multiple parameters, a function call may need multiple arguments.
- ways to pass arguments to functions:
  - *positional arguments* = need to be in the same order the parameters were written.

  - *keyword arguments* = each argument consists of a variable name and a value; and lists and dictionaries of values.

### Positional Arguments

When call a function, Python must match each argument in the function call with a parameter in the function definition.

based on the order of the arguments provided. Values matched up this way are called positional arguments.

page 150 (skipped!!)

## Storing Your Functions in Modules

Functions advantages:

- by way of separating blocks of code from main program.
- By using descriptive names for functions.

Store functions in a separate file called a *module* and then *importing* that module into the main program. An `import` statement tells Python to make the code in a module available in the currently running program file.

- storing allows to hide the details of program's code and focus on higher-level logic.
- allows to reuse functions in many differet programs.
- can share those separate files with others without having to share the entire program.

**Ways to import a module:**

### Importing an Entire Module

First, we need to create a *module* that is a file ending in *.py* containing the code that you want to import intor your program.

To make this module, create a file *pizza.py* with this function `make_pizza()`:

```python
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
```

Then, make a separate file called *making_pizzas.py* in the same directory as *pizza.py* and makes two calls to `make_pizza()`:

```python
import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```
