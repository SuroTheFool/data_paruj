# Lab Overview :

The Final Goal  of this lab is to give us proeficiency in using OOP & GIT commands to learn about the first steps of handling a project.
But we can say that this lab is also about how to handle data from a CSV file and use it to answer question as if we were using Excel or google sheets.

# Project Structure  :

```
oop_lab_1/
│
├── README.md                 # This file
├── Cities.csv                      # The dataset
|── data_processing.py	  # The analysis code

```

# Design Overview

## class DataLoader (Given with the starting code.)
### ```def __init__``` method :
Look if the path exist.
### ```load_csv``` method :
Loading my csv file with the built-in python function : open() 

## class Table (My main work during the lab.) :

### ```def __init__``` : create 2 instance values for my class : "name", "table"
First instance to give a name to my object, the seconde one is to use my loaded file variable
### ```def filter``` : create 1 arguments for my class : "preidcate"
I use predicate to add a condition, For example : "I want to print all cities from germany"

### ```aggregate``` : create 2 arguments for my class : ;"func", "column"

func is used for lambda in my program, and the argument "column" to specify which column i want to choose in my dict.

# How to test and run your code
To run my program please use this command :
 ```cmd
 python3 data_processing.py 
 ``` 

