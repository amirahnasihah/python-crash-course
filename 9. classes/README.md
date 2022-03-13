# CHAPTER 9: CLASSES

_Object-oriented programming_ is one of the most effective approaches to writing software. In object-oriented programming you write _classes_ that represent real-world things and situations, and you create _objects_ based on these classes. When you write a class, you define the general behavior that a whole category of objects can have.

When you create individual objects from the class, each object is automatically equipped with the general behavior; you can then give each object whatever unique traits you desire. You’ll be amazed how well real-world situations can be modeled with object-oriented programming.

Making an object from a class is called _instantiation_, and you work with _instances_ of a class. In this chapter you’ll write classes and create instances of those classes. You’ll specify the kind of information that can be stored in instances, and you’ll define actions that can be taken with these instances. Object-oriented programming is one of the
most effective approaches to writing software.
In object-oriented programming you
write classes that represent real-world things
and situations, and you create objects based on these
classes. When you write a class, you define the general
behavior that a whole category of objects can have.
When you create individual objects from the class, each object is automatically
equipped with the general behavior; you can then give each object
whatever unique traits you desire. You’ll be amazed how well real-world
situations can be modeled with object-oriented programming.
Making an object from a class is called instantiation, and you work with
instances of a class. In this chapter you’ll write classes and create instances
of those classes. You’ll specify the kind of information that can be stored in
instances, and you’ll define actions that can be taken with these instances.

## Creating and Using a Class

You can model almost anything using classes. Let’s start by writing a simple class, Dog, that represents a dog—not one dog in particular, but any dog.

### Creating the Dog Class

Each instance created from the `Dog` class will store a `name` and an `age`, and we’ll give each dog the ability to `sit()` and `roll_over()`:

```python
class Dog:  #1
    """A simple attempt to model a dog."""  #2

    def __init__(self, name, age): #3
        """Initialize name and age attributes."""
        self.name = name    #4
        self.age = age

    def sit(self):  #5
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")
```

- at **#1**, we define a class called `Dog`. By convention, capitalized names refer to classes in Python. There are no parentheses in the class definition because we’re creating this class from scratch.
- At **#2**, we write a docstring describing what this class does.

**The `__init__()` Method**

A function that’s part of a class is a method. Everything you learned about functions applies to methods as well; the only practical difference for now is the way we’ll call _methods_. The `__init__()` method at **#3** is a special method that Python runs automatically whenever we create a new instance based on the Dog class. This method has two leading underscores and two trail-ing underscores, a convention that helps prevent Python’s default method names from conflicting with your method names. Make sure to use two underscores on each side of `__init__()`. If you use just one on each side, the method won’t be called automatically when you use your class, which can result in errors that are difficult to identify.

We define the `__init__()` method to have three parameters: `self`, `name`, and `age`. The `self` parameter is required in the method definition, and it must come first before the other parameters. It must be included in the def-inition because when Python calls this method later (to create an instance of `Dog`), the method call will automatically pass the `self` argument. Every method call associated with an instance automatically passes `self`, which is a reference to the instance itself; it gives the individual instance access to the attributes and methods in the class. When we make an instance of `Dog`, Python will call the `__init__()` method from the `Dog` class. We’ll pass `Dog()` a name and an age as arguments; `self` is passed automatically, so we don’t need to pass it. Whenever we want to make an instance from the `Dog` class, we’ll provide values for only the last two parameters, `name` and `age`.

The two variables defined at **#4** each have the prefix `self`. Any variable prefixed with `self` is available to every method in the class, and we’ll also be able to access these variables through any instance created from the class. The line `self.name = name` takes the value associated with the parameter `name` and assigns it to the variable `name`, which is then attached to the instance being created. The same process happens with `self.age = age`. Variables that are accessible through instances like this are called _attributes_.
The Dog class has two other methods defined: `sit()` and `roll_over()` **#5**. Because these methods don’t need additional information to run, we just define them to have one parameter, `self`. The instances we create later will have access to these methods. In other words, they’ll be able to sit and roll over. For now, `sit()` and `roll_over()` don’t do much. They simply print a message saying the dog is sitting or rolling over. But the concept can be extended to realistic situations: if this class were part of an actual com-puter game, these methods would contain code to make an animated dog sit and roll over. If this class was written to control a robot, these methods would direct movements that cause a robotic dog to sit and roll over.

#### Making an Instance from a Class

Think of a class as a set of instructions for how to make an instance. The class `Dog` is a set of instructions that tells Python how to make individual instances representing specific dogs.

```python
class Dog:
    --snip--

my_dog = Dog('Willie', 6)   #1

print(f"My dog's name is {my_dog}.")    #2
print(f"My dog is {my_dog.age} years old.") #3
```

- at **#1**, create a dog named `'Willie'` and age is `6`. When Python reads this line, it calls the `__init__`() method in `Dog` with the arguments `'Willie'` and `6`. The `__init__`() method creates an instance representing this particular dog and sets the `name` and `age` attributes using the values we provided. Python then returns an instance representing this dog. We assign that instance to the variable `my_dog`. The naming convention is helpful here: we can usually assume that a capitalized name like `Dog` refers to a class, and a lowercase name like `my_dog` refers to a single instance
created from a class.

### Accessing Attributes

To access the attributes of an instance, you use dot notation. At **#2** we access the value of `my_dog`’s attribute `name` by writing:

```python
my_dog.name
```

This syntax demonstrates how  Python finds an attribute’s value. Here Python looks at the instance `my_dog` and then finds the attribute name associated with my_dog. This is the same attribute referred to as `self.name` in the class `Dog`.
At **#3** we use the same approach to work with the attribute `age`.
Output:

```python
My dog's name is Willie.
My dog is 6 years old.
```

### Calling Methods

After we create an instance from the class `Dog`, we can use _dot_ notation to call any method defined in `Dog`. Let’s make our dog sit and roll over:

```python
class Dog:
--snip--

my_dog = Dog('Willie', 6)
my_dog.sit()
my_dog.roll_over()
```

To call a method, give the name of the instance (in this case, `my_dog`) and the method you want to call, separated by a dot. When Python reads `my_dog.sit`(), it looks for the method sit() in the class `Dog` and runs that code. Python interprets the line `my_dog.roll_over`() in the same way.
Now Willie does what we tell him to:

```python
Willie is now sitting.
Willie rolled over!
```

**Creating Multiple Instances**
You can create as many instances from a class as you need. Let’s create a second dog called `your_dog`:

```python
class Dog:
--snip--
my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
```

Output:

```python
My dog's name is Willie.
My dog is 6 years old.
Willie is now sitting.

Your dog's name is Lucy.
Your dog is 3 years old.
Lucy is now sitting.
```

Even if we used the same name and age for the second dog, Python would still create a separate instance from the Dog class. You can make as many instances from one class as you need, as long as you give each instance a unique variable name or it occupies a unique spot in a list or dictionary.

## Working with Classes and Instances

You’ll want to do is modify the attributes associated with a particular instance. You can modify the attributes of an instance directly or write methods that update attributes in specific ways.

### The Car Class

```python
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):  #1
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self): #2
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.manufacturer} {self.model}"
        return long_name.title()

my_new_car = Car('audi', 'a4', 2019)    #3
print(my_new_car.get_descriptive_name())
```

At **#1** in the `Car` class, we define the `__init__`() method with the `self` parameter first, just like we did before with our Dog class. We also give it three other parameters: `make`, `model`, and `year`. The `__init__`() method takes in these parameters and assigns them to the attributes that will be associated with instances made from this class. When we make a new `Car` instance, we’ll need to specify a make, model, and year for our instance.
At **#2** we define a method called `get_descriptive_name`() that puts a car’s `year`, `make`, and `model` into one string neatly describing the car. This will spare us from having to print each attribute’s value individually. To work with the attribute values in this method, we use `self.make`, `self.model`, and `self.year`.
At **#3** we make an instance from the Car class and assign it to the variable `my_new_car`. Then we call `get_descriptive_name`() to show what kind of car we have:

Output:

```python
2019 Audi A4
```

To make the class more interesting, let’s add an attribute that changes over time. We’ll add an attribute that stores the car’s overall mileage.

#### Setting a Default Value for an Attribute

When an instance is created, attributes can be defined without being passed in as parameters. These attributes can be defined in the `__init__`() method, where they are assigned a default value.
Let’s add an attribute called `odometer_reading` that always starts with a value of `0`. We’ll also add a method `read_odometer`() that helps us read each car’s odometer:

```python
class Car:

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0   #1

    def get_descriptive_name(self):
        --snip--

    def read_odometer(self):    #2
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
```

This time when Python calls the `__init__`() method to create a new instance, it stores the make, model, and year values as attributes like it did in the previous example. Then Python creates a new attribute called `odometer_reading` and sets its initial value to `0` **#1**. We also have a new method called `read_odometer`() at **#2** that makes it easy to read a car’s mileage.

Our car starts with a mileage of 0:

```python
2019 Audi A4
This car has 0 miles on it.
```

Not many cars are sold with exactly 0 miles on the odometer, so we need a way to change the value of this attribute.

#### Modifying Attribute Values

You can change an attribute’s value in _three ways_: you can change the value _directly_ through an instance, set the value through a _method_, or _increment_ the value (add a certain amount to it) through a method. Let’s look at each of these approaches.

### Modifying an Attribute’s Value Directly

The simplest way to modify the value of an attribute is to access the attribute directly through an instance. Here we set the odometer reading to 23 directly:

```python
class Car:
    --snip--

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23    #1
my_new_car.read_odometer()
```

At **#1** we use dot notation to access the car’s `odometer_reading` attribute and set its value directly. This line tells Python to take the instance `my_new_car`, find the attribute `odometer_reading` associated with it, and set the value of that attribute to `23`:

```python
2019 Audi A4
This car has 23 miles on it.
```

### Modifying an Attribute’s Value Through a Method

Pass the new value to a method that handles the updating _internally_.
Here’s an example showing a method called `update_odometer`():

```python
class Car:
    --snip--

    def update_odometer(self, mileage):     #1
        """Set the odometer reading to the given value."""
        self.odometer_reading = mileage

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23)  #2
my_new_car.read_odometer()
```

The only modification to `Car` is the addition of `update_odometer`() at **#1**. This method takes in a mileage value and assigns it to `self.odometer_reading`.

At **#2** we call `update_odometer`() and give it `23` as an argument (corresponding to the `mileage` parameter in the method definition). It sets the odometer reading to 23, and `read_odometer`() prints the reading:

```python
2019 Audi A4
This car has 23 miles on it.
```

We can extend the method `update_odometer`() to do additional work every time the odometer reading is modified. Let’s add a little logic to make sure no one tries to roll back the odometer reading:

```python
class Car:
    --snip--

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:    #1
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")   #2
```

Now `update_odometer`() checks that the new reading makes sense before modifying the attribute. If the new mileage, mileage, is greater than or equal to the existing mileage, `self.odometer_reading`, you can update the odometer reading to the new mileage **#1**. If the new mileage is less than the existing mileage, you’ll get a warning that you can’t roll back an odometer **#2**.

### Incrementing an Attribute’s Value Through a Method

Increment an attribute’s value by a certain amount rather than set an entirely new value. Say we buy a used car and put 100 miles on it between the time we buy it and the time we register it.

```python
class Car:
    --snip--

    def update_odometer(self, mileage):
        --snip--

    def increment_odometer(self, miles):    #1
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

my_used_car = Car('subaru', 'outback', 2015)    #2
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500) #3
my_used_car.read_odometer()

my_used_car.increment_odometer(100) #4
my_used_car.read_odometer()
```

The new method `increment_odometer`() at **#1** takes in a number of miles, and adds this value to `self.odometer_reading`. At **#2** we create a used car, `my_used_car`. We set its odometer to 23,500 by calling `update_odometer`() and passing it 23_500 at **#3**. At **#4** we call `increment_odometer`() and pass it 100 to add the 100 miles that we drove between buying the car and registering it:

```python
2015 Subaru Outback
This car has 23500 miles on it.
This car has 23600 miles on it.
```

You can easily modify this method to reject negative increments so no one uses this function to roll back an odometer.

NOTE
>You can use methods like this to control how users of your program update values such as an odometer reading, but anyone with access to the program can set the odometer reading to any value by accessing the attribute directly.

## Inheritance

If the class
you’re writing is a specialized version of another class you wrote, you can use _inheritance_. When one class _inherits_ from another, it takes on the attributes and methods of the first class. The original class is called the _parent class_, and the new class is the _child class_. The child class can inherit any or all of the attributes and methods of its parent class, but it’s also free to define new attributes and methods of its own.

### The `__init__`() Method for a Child Class

When you’re writing a new class based on an existing class, you’ll often want to call the `__init__`() method from the parent class. This will initialize any attributes that were defined in the parent `__init__`() method and make them available in the child class.
As an example, let’s model an _electric_car.py_.
Let’s start by making a simple version of the `ElectricCar` class, which does everything the `Car` class does:

```python
class Car:  #1
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.manufacturer} {self.model}"
        return long_name.title()

    def read_odometer(self):
    print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

class ElectricCar(Car): #2
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):  #3
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year) #4

my_tesla = ElectricCar('tesla', 'model s', 2019)    #5
print(my_tesla.get_descriptive_name())
```

At **#1** we start with `Car`. When you create a child class, the parent class must be part of the current file and must appear before the child class in the file. At **#2** we define the child class, `ElectricCar`. The name of the par-ent class must be included in parentheses in the definition of a child class. The `__init__`() method at **#3** takes in the information required to make a `Car` instance.

The `super`() function at **#4** is a special function that allows you to call a method from the parent class. This line tells Python to call the `__init__`() method from `Car`, which gives an `ElectricCar` instance all the attributes defined in that method. The name _super_ comes from a convention of calling the parent class a _superclass_ and the child class a _subclass_.

We test whether inheritance is working properly by trying to create an electric car with the same kind of information we’d provide when making a regular car. At **#5** we make an instance of the `ElectricCar` class and assign it to `my_tesla`. This line calls the `__init__`() method defined in `ElectricCar`, which in turn tells Python to call the `__init__`() method defined in the parent class `Car`. We provide the arguments `'tesla'`, `'model s'`, and `2019`.
Aside from `__init__`(), there are no attributes or methods yet that are particular to an electric car. At this point we’re just making sure the electric car has the appropriate `Car` behaviors:

```python
2019 Tesla Model S 
```

The ElectricCar instance works just like an instance of Car, so now we can begin defining attributes and methods specific to electric cars.

#### Defining Attributes and Methods for the Child Class

Once you have a child class that inherits from a parent class, you can add any new attributes and methods necessary to differentiate the child class from the parent class.

Let’s add an attribute that’s specific to electric cars (a battery, for example) and a method to report on this attribute. We’ll store the battery size and write a method that prints a description of the battery:

```python
class Car:
    --snip--

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery_size = 75  #1

    def describe_battery(self): #2
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
```

At **#1** we add a new attribute `self.battery_size` and set its initial value to, say, `75`. This attribute will be associated with all instances created from the `ElectricCar` class but won’t be associated with any instances of `Car`. We also add a method called `describe_battery`() that prints information about the battery at **#2**. When we call this method, we get a description that is clearly specific to an electric car:

```python
2019 Tesla Model S 
This car has a 75-kWh battery.
```

There’s no limit to how much you can specialize the `ElectricCar` class. You can add as many attributes and methods as you need.

#### Overriding Methods from the Parent Class

You can _override_ any method from the parent class that doesn’t fit what you’re trying to model with the child class. To do this, you define a method in the child class with the same name as the method you want to override in the parent class. Python will disregard the parent class method and only pay attention to the method you define in the child class.
Say the class Car had a method called `fill_gas_tank`(). This method is meaningless for an all-electric vehicle, so you might want to override this method. Here’s one way to do that:

```python
class ElectricCar(Car):
    --snip--

def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")
```

Now if someone tries to call `fill_gas_tank`() with an electric car, Python will ignore the method `fill_gas_tank`() in `Car` and run this code instead. When you use inheritance, you can make your child classes retain what you need and override anything you don’t need from the parent class.

#### Instances as Attributes

When modeling something from the real world in code, you may find that you’re adding more and more detail to a class. You’ll find that you have a growing list of attributes and methods and that your files are becoming lengthy. In these situations, you might recognize that part of one class can be written as a separate class. You can break your large class into smaller classes that work together.

For example, if we continue adding detail to the `ElectricCar` class, we might notice that we’re adding many attributes and methods specific to the car’s battery. When we see this happening, we can stop and move those attributes and methods to a separate class called `Battery`. Then we can use a `Battery` instance as an attribute in the `ElectricCar` class:

```python
class Car:
    --snip--

class Battery:  #1
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):    #2
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self): #3
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()    #4

my_tesla = ElectricCar('tesla', 'model s', 2019)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
```

At **#1** we define a new class called `Battery` that doesn’t inherit from any other class. The `__init__`() method at **#2** has one parameter, `battery_size`, in addition to `self`. This is an optional parameter that sets the battery’s size to 75 if no value is provided. The method `describe_battery`() has been moved to this class as well **#3**.
In the `ElectricCar` class, we now add an attribute called `self.battery` **#4**. This line tells Python to create a new instance of `Battery` (with a default size of 75, because we’re not specifying a value) and assign that instance to the attribute `self.battery`. This will happen every time the `__init__`() method is called; any `ElectricCar` instance will now have a `Battery` instance created automatically.

We create an electric car and assign it to the _variable_ `my_tesla`. When we want to describe the battery, we need to work through the car’s battery attribute:

```python
my_tesla.battery.describe_battery()
```

This line tells Python to look at the instance `my_tesla`, find its battery attribute, and call the method `describe_battery`() that’s associated with the `Battery` instance stored in the attribute.

Output is identical to previously:

```python
2019 Tesla Model S
This car has a 75-kWh battery.
```

This looks like a lot of extra work, but now we can describe the battery in as _much detail_ as we want without cluttering the `ElectricCar` class. Let’s add another method to `Battery` that reports the _range_ of the car based on the battery size:

```python
class Car:
    --snip--

class Battery:
    --snip--

    def get_range(self):    #1
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car):
    --snip--

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()    #2
```

The new method `get_range`() at **#1** performs some simple analysis. If the battery’s capacity is 75 kWh, `get_range`() sets the range to 260 miles, and if the capacity is 100 kWh, it sets the range to 315 miles. It then reports this value. When we want to use this method, we again have to call it through the car’s battery attribute at **#2**.

Output tells us the range of the car based on its battery size:

```python
2019 Tesla Model S
This car has a 75-kWh battery.
This car can go about 260 miles on a full charge.
```

#### Modeling Real-World Objects

As you begin to model more complicated things like electric cars, you’ll wrestle with interesting questions. Is the range of an electric car a property of the battery or of the car? If we’re only describing one car, it’s probably fine to maintain the association of the method get_range() with the Battery class. But if we’re describing a manufacturer’s entire line of cars, we proba-bly want to move get_range() to the ElectricCar class. The get_range() method would still check the battery size before determining the range, but it would report a range specific to the kind of car it’s associated with. Alternatively, we could maintain the association of the get_range() method with the bat-tery but pass it a parameter such as car_model. The get_range() method would then report a range based on the battery size and car model.

This brings you to an interesting point in your growth as a program-mer. When you wrestle with questions like these, you’re thinking at a higher logical level rather than a syntax-focused level. You’re thinking not about Python, but about how to represent the real world in code. When you reach this point, you’ll realize there are often no right or wrong approaches to modeling real-world situations. Some approaches are more efficient than others, but it takes practice to find the most efficient representations. If your code is working as you want it to, you’re doing well! Don’t be discour-aged if you find you’re ripping apart your classes and rewriting them several times using different approaches. In the quest to write accurate, efficient code, everyone goes through this process.

## Importing Classes

As you add more functionality to your classes, your files can get long, even when you use inheritance properly. In keeping with the overall philosophy of Python, you’ll want to keep your files as _uncluttered_ as possible. To help, Python lets you store classes in modules and then import the classes you need into your main program.

### Importing a Single Class

Let’s create a module containing just the `Car` class. This brings up a subtle naming issue: we already have a file named _car.py_ in this chapter, but this module should be named _car.py_ because it contains code representing a car. We’ll resolve this naming issue by storing the `Car` class in a module named _car.py_, replacing the _car.py_ file we were previously using. From now on, any program that uses this module will need a more specific filename, such as _my_car.py_. Here’s _car.py_ with just the code from the class `Car`:

```python
"""A class that can be used to represent a car."""  #1

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.manufacturer} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

        def increment_odometer(self, miles):
            """Add the given amount to the odometer reading."""
            self.odometer_reading += miles
```

At **#1** we include a module-level docstring that briefly describes the contents of this module. You should write a docstring for each module you create.

Now we make a separate file called _my_car.py_. This file will import the `Car` class and then create an instance from that class:

```python
from car import Car #1

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()
```

The import statement at **#1** tells Python to open the car module and import the class `Car`. Now we can use the `Car` class as if it were defined in this file. The output is the same as we saw earlier:

```python
2019 Audi A4
This car has 23 miles on it.
```

Importing classes is an effective way to program. Picture how long this program file would be if the entire `Car` class were included. When you instead move the class to a module and import the module, you still get all the same functionality, but you keep your main program file clean and easy to read. You also store most of the logic in separate files; once your classes work as you want them to, you can leave those files alone and focus on the higher-level logic of your main program.

#### Storing Multiple Classes in a Module

You can store as many classes as you need in a single module, although each class in a module should be related somehow. The classes `Battery` and `ElectricCar` both help represent cars, so let’s add them to the module _car.py_.

```python
"""A set of classes used to represent gas and electric cars."""

class Car:
    --snip--

class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car):
    """Models aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()
```

Now we can make a new file called _my_electric_car.py_, import the `ElectricCar` class, and make an electric car:

```python
from car import ElectricCar

my_tesla = ElectricCar('tesla', 'model s', 2019)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
```

This has the same output we saw earlier, even though most of the logic is hidden away in a module:

```python
2019 Tesla Model S
This car has a 75-kWh battery.
This car can go about 260 miles on a full charge.
```

#### Importing Multiple Classes from a Module

You can import as many classes as you need into a program file. If we want to make a regular car and an electric car in the same file, we need to import both classes, Car and ElectricCar:

```python
from car import Car, ElectricCar    #1

my_beetle = Car('volkswagen', 'beetle', 2019)   #2
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2019)   #3
print(my_tesla.get_descriptive_name())
```

You import multiple classes from a module by separating each class with a comma **#1**. Once you’ve imported the necessary classes, you’re free to make as many instances of each class as you need.

In this example we make a regular Volkswagen Beetle at **#2** and an electric
Tesla Roadster at **#3**:

```python
2019 Volkswagen Beetle
2019 Tesla Roadster
```

#### Importing an Entire Module

You can also import an entire module and then access the classes you need using dot notation. This approach is simple and results in code that is easy to read. Because every call that creates an instance of a class includes the module name, you won’t have naming conflicts with any names used in the current file.
Here’s what it looks like to import the entire car module and then create a regular car and an electric car:

```python
import car  #1

my_beetle = car.Car('volkswagen', 'beetle', 2019)   #2
print(my_beetle.get_descriptive_name())

my_tesla = car.ElectricCar('tesla', 'roadster', 2019)   #3
print(my_tesla.get_descriptive_name())
```

At **#1** we import the entire car module. We then access the classes we need through the `module_name.ClassName` syntax. At **#2** we again create a Volkswagen Beetle, and at **#3** we create a Tesla Roadster.

#### Importing All Classes from a Module

You can import every class from a module using the following syntax:

```python
from module_name import *
```

This method is not recommended for two reasons. First, it’s helpful to be able to read the `import` statements at the top of a file and get a clear sense of which classes a program uses. With this approach it’s unclear which classes you’re using from the module. This approach can also lead to confusion with names in the file. If you accidentally import a class with the same name as something else in your program file, you can create errors that are hard to diagnose. I show this here because even though it’s not a recommended approach, you’re likely to see it in other people’s code at some point.
If you need to import many classes from a module, you’re better off importing the entire module and using the `module_name.ClassName` syntax. You won’t see all the classes used at the top of the file, but you’ll see clearly where the module is used in the program. You’ll also avoid the potential naming conflicts that can arise when you import every class in a module.

#### Importing a Module into a Module

Sometimes you’ll want to spread out your classes over several modules to keep any one file from growing too large and avoid storing unrelated classes in the same module. When you store your classes in several modules, you may find that a class in one module depends on a class in another module. When this happens, you can import the required class into the first module.

For example, let’s store the `Car` class in one module and the `ElectricCar` and Battery classes in a separate module. We’ll make a new module called _electric_car.py_—replacing the _electric_car.py_ file we created earlier—and copy just the `Battery` and `ElectricCar` classes into this file:

```python
"""A set of classes that can be used to represent electric cars."""

from car import Car #1

class Battery:
    --snip--

class ElectricCar(Car):
    --snip--
```

The class `ElectricCar` needs access to its parent class `Car`, so we import `Car` directly into the module at **#1**. If we forget this line, Python will raise an error when we try to import the `electric_car` module. We also need to update the `Car` module so it contains only the `Car` class:

```python
"""A class that can be used to represent a car."""

class Car:
    --snip--
```

Now we can import from each module separately and create whatever kind of car we need:

```python
from car import Car #1
from electric_car import ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())
```

At **#1** we import `Car` from its module, and `ElectricCar` from its module. We then create one regular car and one electric car. Both kinds of cars are created correctly:

```python
2019 Volkswagen Beetle
2019 Tesla Roadster
```

#### Using Aliases

As you saw in Chapter 8, aliases can be quite helpful when using modules to organize your projects’ code. You can use aliases when importing classes as well.

As an example, consider a program where you want to make a bunch of electric cars. It might get tedious to type (and read) `ElectricCar` over and over again. You can give `ElectricCar` an alias in the import statement:

```python
from electric_car import ElectricCar as EC
```

Now you can use this alias whenever you want to make an electric car:

```python
my_tesla = EC('tesla', 'roadster', 2019)
```

#### Finding Your Own Workflow

As you can see, Python gives you many options for how to structure code in a large project. It’s important to know all these possibilities so you can determine the best ways to organize your projects as well as understand other people’s projects.

When you’re starting out, keep your code structure simple. Try doing everything in one file and moving your classes to separate modules once everything is working. If you like how modules and files interact, try storing your classes in modules when you start a project. Find an approach that lets you write code that works, and go from there.

## The Python Standard Library

The _Python standard library_ is a set of modules included with every Python installation. Now that you have a basic understanding of how functions and classes work, you can start to use modules like these that other programmers have written. You can use any function or class in the standard library by including a simple `import` statement at the top of your file. Let’s look at one module, `random`, which can be useful in modeling many real-world situations.
One interesting function from the random module is `randint()`. This function takes two integer arguments and returns a randomly selected integer between (and including) those numbers.

Here's how to generate a random numbers between 1 and 6:

```python
>>> from random import choice
>>> players = ['charles', 'martina', 'michael', 'florence', 'eli']
>>> first_up = choice(players)
>>> first_up
'florence'
```

The `random` module shouldn’t be used when building security-related applications, but it’s good enough for many fun and interesting projects.

NOTE
> Can also download modules from external sources. You’ll see a number of these examples in _Part II_, where we’ll need external modules to complete each project.

## Styling Classes

A few styling issues related to classes are worth clarifying, especially as your programs become more complicated.

Class names should be written in _**CamelCase**_. To do this, capitalize the first letter of each word in the name, and don’t use underscores. Instance and module names should be written in lowercase with underscores between words.

Every class should have a docstring immediately following the class definition. The docstring should be a brief description of what the class does, and you should follow the same formatting conventions you used for writing docstrings in functions. Each module should also have a docstring describing what the classes in a module can be used for.

You can use blank lines to organize code, but don’t use them excessively. Within a class you can use one blank line between methods, and within a module you can use two blank lines to separate classes.

If you need to import a module from the standard library and a module that you wrote, place the import statement for the standard library module first. Then add a blank line and the import statement for the module you wrote. In programs with multiple import statements, this convention makes it easier to see where the different modules used in the program come from.

## Summary

In this chapter you learned how to write your own classes. You learned how to store information in a class using attributes and how to write methods that give your classes the behavior they need. You learned to write `__init__`() methods that create instances from your classes with exactly the attributes you want. You saw how to modify the attributes of an instance directly and through methods. You learned that inheritance can simplify the creation of classes that are related to each other, and you learned to use instances of one class as attributes in another class to keep each class simple.
You saw how storing classes in modules and importing classes you need into the files where they’ll be used can keep your projects organized. You started learning about the Python standard library, and you saw an example based on the `random` module. Finally, you learned to style your classes using Python conventions.
In Chapter 10 you’ll learn to work with files so you can save the work you’ve done in a program and the work you’ve allowed users to do. You’ll also learn about _exceptions_, a special Python class designed to help you respond to errors when they arise.
