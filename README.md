# MyWatchList
## Video Demo:  <https://www.youtube.com/watch?v=0VgKTzB-sv4>
## Description :
Hi ,This is my CS50p Final Project - MyWatchList. This program helps you in making your own list of things you have watched and add the status of the show or movie in terms of how much you've watched and also especially rate your experiance with it.

The Data you enter is stored in a .csv file and the program will also let you add to the watchlist, update the watchlist, delete something from the watchlist, or view your data in a tabulated form and most importantly you can create as many Watchlists as you want with .csv file name you want.

## How it works :
```
get_key()
```
`get_key()` function with no parameter which as the name sugests gets a key as the input in this case which will be a single character by first printing the instructions as a table using `tabulate` module which consists of what each character does namely C,A,V,D,U,E. And if the user inputs anything other than the character from the instruction table the program will exit with a `sys.exit` specifying an `Invalid Key` was entered.

```
switch()
```
`switch()` function at first was just a fuction that implements a fuction for each key by using `if-else` but after i finished everything
i wanted functions to accept parameters and return something just so i can have a test file for the project and so `switch()` became like a sudden protogonist of my project.

`switch()` is a fuction which gets the input required by the functions for each keys and gives it to the respective key's functions as parameters.

```
check_input()
```

`check_input()` fuction gets  a name as its parameter and using `glob module` it returns a boolean value `True` if name.csv is not already present and `False` if it is.

```
key_C()
```
`key_C()` fuction gets a parameter called name which is a name for the .csv file that is created for the watchlist and this .csv file will be a new file and not someother .csv file thats already in your pc,this is done using the `check_input()` function.

It creates and writes the headers for the watchlist on the .csv file with the given name parameter.

```
key_A()
```
`key_A()` function gets the following parameters:

`name` = name of the .csv file that already exists

`sno` = serial number is like a number that represents the row the upcoming data is gonna be in(can give any number).

`_name` = name of the show or movie

`status` = your current status of watching the show like Completed,On Hold or Dropped.

`rating` = your rating for the show or movie.

These datas are then added to the .csv file as a single row.

```
key_U()
```
`key_U()` function is used to update the watchlist using the `pandas` module that needs to be installed before running the program.
for more info regarding installation scroll down to the `Installation` section.

```
key_D()
```
`key_D()` function is used to delete a row from the .csv file and this function also uses `pandas` module.
```
view()
```
`view()` function gets the name of the .csv file as a parameter and returns it as a table using the `tabulate` module.
## Installation
Use [pip](https://pip.pypa.io/en/stable/) to install the package `tabulate`
```
$ pip install tabulate
```

Use [pip](https://pip.pypa.io/en/stable/) to install the package `pandas`
```
$ pip install pandas
```
## To Run The Program
### Use [python](https://www.python.org/) to run the application
```
$ python project.py
```
### Use [pytest](https://docs.pytest.org/en/7.2.x/) to test the application
```
$ pytest test_project.py
```
