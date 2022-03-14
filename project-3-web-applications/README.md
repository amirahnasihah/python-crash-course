# Web Applications

In the Web Applications project (Chapters 18, 19, and 20), you’ll use the Django package to create a simple web application that allows users to keep a journal about any number of topics they’ve been learning about. Users will create an account with a username and password, enter a topic, and then make entries about what they’re learning. You’ll also learn how to deploy your app so anyone in the world can access it.

After completing this project, you’ll be able to start building your own simple web applications, and you’ll be ready to delve into more thorough resources on building applications with Django.

## Django

- Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.

### Virtual environment?

- A virtual environment is simply a tool that separates the dependencies of different projects by creating a separate isolated environment for each project.
- These are simply the directories so that unlimited virtual environments can be created. This is one of the popular tools used by most of the Python developers.

To set up a virtual environment, use the following steps.

### Getting started (Windows PowerShell)

> First step

Open terminal/powershell - search for Command Prompt or Windows PowerShell:

Change directory to external drive (D:) _*optional_

```sys
PS C:\Users\surface3> d:
```

Then, create a new directory/folder named _learning_log_:

```sys
PS D:\> mkdir learning_log
```

After create a new directory for the project called learning_log, switch to that directory in a terminal:

```sys
PS D:\> cd d:\learning_log
PS D:\learning_log>
```

> Creating a Virtual Environment

And enter the following code to create a virtual environment:

```sys
PS D:\learning_log> python -m venv ll_env
```

> Activating the Virtual Environment

If you’re using PowerShell, might need to capitalize Activate. Also have to deal on Execution Policy see [HERE.](https://adamtheautomator.com/run-powershell-script/)

Getting know more of Windows PowerShell [docs.](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.2#:~:text=PowerShell%27s%20execution%20policy%20is%20a,the%20execution%20of%20malicious%20scripts.)

Restricted  is the default policy set for Windows client computers. Can still execute individual commands in a terminal, but not a script file including formatting and configuration files (`.ps1xml`), module script files (`.psm1`), and PowerShell profiles (`.ps1`).

- Type `Set-ExecutionPolicy` RemoteSigned to set the policy to RemoteSigned
- Type `Set-ExecutionPolicy` Unrestricted to set the policy to Unrestricted

Using a **RemoteSigned** policy would be an ideal option when running a script downloaded from the internet:

```sys
PS D:\learning_log> Set-ExecutionPolicy RemoteSigned
```

Now **activate** the virtual environment using the command:

```sys
PS D:\learning_log> ll_env\Scripts\Activate
```

To stop using a virtual environment, enter **deactivate**. The environment will also become inactive when you close the terminal:

```sys
PS D:\learning_log> ll_env\Scripts\deactivate
```

> Installing Django

Once the virtual environment is activated, enter the following to install Django and wait for the successfully installed:

```sys
(ll_env) PS D:\learning_log> pip install django
>>> Installing collected packages: pytz, django
>>> Successfully installed django-
```

> Creating a Project in Django

The command tells Django to set up a new project called _learning_log_. The dot at the end of the command creates the new project with a directory structure that will make it easy to deploy the app to a server when we’re finished developing it:

Don’t forget this `dot`, or might run into some configuration issues when deploy the app. If forget the dot, delete the files and folders that were created (except ll_env), and run the command again.

```sys
(ll_env) PS D:\learning_log> django-admin startproject learning_log .
(ll_env) PS D:\learning_log> ls (or dir on Windows)
>>> learning_log ll_env manage.py
(ll_env) PS D:\learning_log> ls learning_log (or dir on Windows)
>>> __init__.py settings.py urls.py wsgi.py
```

- _learning_log_ = Django created a new directory called learning_log
- _manage.py_ = is a short program that takes in commands and feeds them to the relevant part of Django to run them. Will use these commands to manage tasks, such as working with databases and running servers.
- _learning_log_ directory contains four files, three most importants:
  - _settings.py_ = controls how Django interacts with the system and manages the project. Will modify a few of these settings and add some settings of our own as the project evolves
  _urls.py_ = tells Django which pages to build in response to browser requests.
  _wsgi.py_ = helps Django serve the files it creates. Filename is an acronym for _web server gateway interface_.

> Creating the Database

Django stores most of the information for a project in a database, so need to create a database that Django can work with.

```sys
(ll_env) PS D:\learning_log> python manage.py migrate
>>> Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  --snip--
Applying sessions.0001_initial... OK
PS D:\learning_log> dir
>>> db.sqlite3 learning_log ll_env manage.py
```

- Any time modify a database, we say we’re _migrating_ the database. Issuing the migrate command for the first time tells Django to make sure the database matches the current state of the project. The first time we run this command in a new project using SQLite.
- Running the `dir` command shows that Django created another file called _db.sqlite3_. 
- SQLite is a database that runs off a single file; it’s ideal for writing simple apps because won’t have to pay much attention to managing the database.

> Viewing the Project

Enter the `runserver` command as follows to view the project in its current state:

```sys
(ll_env) PS D:\learning_log> python manage.py runserver
>>> Watchman unavailable: pywatchman not installed.
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
March 15, 2022 - 03:56:31
Django version 4.0.3, using settings 'learning_log.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

- Django should start a server called the _development server_, so can view the project on your system to see how well it works.
- When you request a page by entering a URL in a browser, the Django server responds to that request by building the appropriate page and sending it to the browser.
- The URL <http://127.0.0.1:8000/> shows that the project is listening for requests on port 8000 on your computer, which is called a localhost.
- The term _localhost_ refers to a server that only processes requests on your system; it doesn’t allow anyone else to see the pages you’re developing.
- Open a web browser and enter the URL <http://localhost:8000/>, or <http://127.0.0.1:8000/> if the first one doesn’t work.
![localhost](https://user-images.githubusercontent.com/89834315/158252674-570cf421-f591-4e12-968e-d4a5c7711a90.jpeg)

