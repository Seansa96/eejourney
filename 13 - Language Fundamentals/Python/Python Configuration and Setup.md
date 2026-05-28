
# How Python treats .py files

Since a Python file can be used in the python shell environment or ran by the Python runtime (the VM with the interpreter), the way Python files are structured is important in defining their behavior.

When Python loads a py file, a special built-in variable called `__name__` is created.

If Python executes this file directly, then `__name__` is set to `__main__`.

If the file is simply imported as a module, then `__name__` is set to the name of the module.

So, the standard convention for setting a python file's entrypoint when it is meant to be executed as a program, is

`if __name__ == "__main__":`

which serves as a guard for that code and keeps it separate and modular, a core tenet of Pythonic scripture.

# User Site

You can see what directories and scripts python is able to import and load during a session by running

`python -m site --user-site`

This prints the location of the site-packages directory on your machine. You may create a `.pth` file here containing the absolute path of whatever scripts you would like to use.

# System Environment Variables

You can also create a `PYTHONPATH` system environment variable, setting the location of whatever scripts you desire as its value, which works similarly as the above.