# Web Applications

In the Web Applications project (Chapters 18, 19, and 20), will use the Django package to create a simple web application that allows users to keep a journal about any number of topics they’ve been learning about. Users will create an account with a username and password, enter a topic, and then make entries about what they’re learning. Will also learn how to deploy an app so anyone in the world can access it.

After completing this project, able to start building own simple web applications, and be ready to delve into more thorough resources on building applications with Django.

## Django

- Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.

### Virtual environment?

- A virtual environment is simply a tool that separates the dependencies of different projects by creating a separate isolated environment for each project.
- These are simply the directories so that unlimited virtual environments can be created. This is one of the popular tools used by most of the Python developers.

To set up a virtual environment, use the following steps.

### Getting started

Step-by-step

- Open terminal/powershell typed Command Prompt or Windows PowerShell
- Change directory to external drive (D:) *optional

```sys
PS C:\Users\surface3> d:
```

- Then, create a new directory/folder named _learning_log_.

```sys
PS D:\> mkdir learning_log
```

- After create a new directory for the project called learning_log, switch to that directory in a terminal

```sys
PS D:\> cd d:\learning_log
PS D:\learning_log>
```

- And enter the following code to create a virtual environment

```sys
PS D:\learning_log> python -m venv ll_env
```
