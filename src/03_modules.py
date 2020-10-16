"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
print('Number of arguments: ' + str(len(sys.argv)))
print('Arguments List: ' + str(sys.argv))
print('-------')
# Print out the OS platform you're using:
print(str(sys.platform))
print('-------')
# Print out the version of Python you're using:
print(str(sys.version))
print('-------')

import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
print(str(os.getpid()))
print('-------')
# Print the current working directory (cwd):
print(str(os.getcwd()))
print('-------')
# Print out your machine's login name
print(str(os.getlogin()))