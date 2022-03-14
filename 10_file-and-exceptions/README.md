# CHAPTER 10: FILES AND EXCEPTIONS

Will learn to work with files so your programs can quickly analyze lots of data. You’ll learn to handle errors so your programs don’t crash when they encounter unexpected situations. You’ll learn about exceptions, which are special objects Python creates to manage errors that arise while a program is running. You’ll also learn about the **json** module, which allows you to save user data so it isn’t lost when your program stops running.

Learning to work with files and save data will make your programs easier for people to use. Users will be able to choose what data to enter and when to enter it. People can run your program, do some work, and then close the program and pick up where they left off later. Learning to handle exceptions will help you deal with situations in which files don’t exist and deal with other problems that can cause your programs to crash. This will make your programs more robust when they encounter bad data, whether it comes from innocent mistakes or from malicious attempts to break your programs. With the skills you’ll learn in this chapter, you’ll make your programs more applicable, usable, and stable.

## Reading from a File

An incredible amount of data is available in text files. Text files can contain weather data, traffic data, socioeconomic data, literary works, and more. Reading from a file is particularly useful in data analysis applications, but it’s also applicable to any situation in which you want to analyze or modify information stored in a file. For example, you can write a program that reads in the contents of a text file and rewrites the file with formatting that allows a browser to display it.

When you want to work with the information in a text file, the first step is to read the file into memory. You can read the entire contents of a file, or you can work through the file one line at a time.

### Reading an Entire File

To begin, we need a file with a few lines of text in it. Let’s start with a file that contains _pi_ to 30 decimal places, with 10 decimal places per line:

```text
3.1415926535 
 8979323846 
 2643383279
```

To try the following examples yourself, you can enter these lines in an editor and save the file as pi_digits.txt, or you can download the file from the book’s resources through _<https://nostarch.com/pythoncrashcourse2e/>_. Save the file in the same directory where you’ll store this chapter’s programs.

Here’s a program that opens this file, reads it, and prints the contents of the file to the screen:

```python
with open('pi_digits.txt') as file_object:
 contents = file_object.read()
print(contents)
```

The first line of this program has a lot going on. Let’s start by looking at the `open()` function. To do any work with a file, even just printing its contents, you first need to _open_ the file to access it. The `open()` function needs one argument: the name of the file you want to open. Python looks for this file in the directory where the program that’s currently being executed is stored. In this example, _file_reader.py_ is currently running, so Python looks for _pi_digits.txt_ in the directory where _file_reader.py_ is stored. The `open()` function returns an object representing the file. Here, `open('pi_digits.txt')` returns an object representing _pi_digits.txt_. Python assigns this object to `file_object`, which we’ll work with later in the program.

The keyword with closes the file once access to it is no longer needed. Notice how we call `open()` in this program but not `close()`. You could open and close the file by calling `open()` and `close()`, but if a bug in your program prevents the `close()` method from being executed, the file may never close. This may seem trivial, but improperly closed files can cause data to be lost or corrupted. And if you call `close()` too early in your program, you’ll find yourself trying to work with a _closed_ file (a file you can’t access), which leads to more errors. It’s not always easy to know exactly when you should close a file, but with the structure shown here, Python will figure that out for you. All you have to do is open the file and work with it as desired, trusting that Python will close it automatically when the `with` block finishes execution.
Once we have a file object representing _pi_digits.txt_, we use the `read()` method in the second line of our program to read the entire contents of the file and store it as one long string in contents. When we print the value of contents, we get the entire text file back:
