
**1.	How python uses the Indentation to control Flow**
<br>

Python uses indentation to the control the flow of code. Each block contains a group of code to be run together. Once a 
separate indentation is made, python will read it as a separate group of code. 
Note that the block must all contain the same amount of indentations to be read together. 
Example layout:
 
Source: https://www.python-course.eu/python3_blocks.php

**2.	Don’t repeat yourself**
The Don’t repeat yourself (DRY) principle in python is necessary in avoiding unnecessary repetition with the code. 
It allows for the code to have a better flow and be easier to read. Another benefit is that if the code needs to be update, 
it will help in reducing additional work needed. 

Example: 
Rather than listing the following separately it could be combined into one listing. 
Original
print(test1)
print(test2)
print(test3)
	DRY Applied
	print(test1,test2,test3)

Source: https://www.earthdatascience.org/courses/earth-analytics-bootcamp/loops/intro-dry-code/

**3.	Design patterns from Gang of Four**
The Gang of Four design patterns are a group of 23 patterns that are the foundation for software design. 
They breakdown into three categories: Creational, Structural, and Behavior.


A singleton pattern which is a creational pattern is a class of which only a single instance can exist. 
Example of Singleton pattern: 
"""
Ensure a class only has one instance, and provide a global point of
access to it.
"""
class Singleton(type):
    """
    Define an Instance operation that lets clients access its unique
    instance.
    """
    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance

class MyClass(metaclass=Singleton):
    """
    Example class.
    """
    pass

def main():
    m1 = MyClass()
    m2 = MyClass()
    assert m1 is m2

if __name__ == "__main__":
    main()

Source: https://www.dofactory.com/net/design-patterns , https://sourcemaking.com/design_patterns/singleton/python/1

**4.	Class**
<br>

A class allows for a way to create objects. It is consider to be the template for creating objects.

Example:
class MyClass:
  x = 5
Source: https://www.learnpython.org/en/Classes_and_Objects

**5.	Object**
<br>

Python is an object oriented programming language. An object is a collection of data (variables) and methods (functions) 
that act on those data. 
Example: 
p1 = MyClass()
print(p1.x)

Source: https://www.w3schools.com/python/python_classes.asp , https://www.programiz.com/python-programming/class

**6.	Static**
<br>

**7.	Property/Attribute**
<br>
In python, everything is an object. And every object has attributes and methods or functions. Attributes are described 
by data variables for example like name, age, height etc.
Properties are special kind of attributes which have getter, setter and delete methods like __get__, __set__ and __delete__ methods.

Source: https://www.tutorialspoint.com/What-is-the-difference-between-attributes-and-properties-in-python


**8.	Method**
<br>

**9.	Exception**
<br>
Exception is an error message within Python that can potential occur when running the program. 
Example:
IOError – which occurs if the file cannot be opened.

Source: https://www.pythonforbeginners.com/error-handling/exception-handling-in-python#:~:targetText=An%20exception%20is%20an%20error,avoids%20your%20program%20to%20crash.

**10.	Unit Test**
<br>
Unit testing is the testing of each unit of software. Each test must be able to be run alone. 
A successful unit test will show “OK” and an unsuccessful test will show either “FAIL” or “ERROR”.

Example: 
import unittest 
  
class SimpleTest(unittest.TestCase): 
  
    # Returns True or False.  
    def test(self):         
        self.assertTrue(True) 
  
if __name__ == '__main__': 
    unittest.main()



Example output:
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK

Source: https://www.geeksforgeeks.org/unit-testing-python-unittest/

**11.	Constructor**
<br>
A constructor is method which is used for initializing the instance variables during object creation. 
There are two types of constructors: default constructor and parameterized constructor.

Example:
class DemoClass:
    # constructor
    def __init__(self):
        # initializing instance variable
        self.num=100

    # a method
    def read_number(self):
        print(self.num)

obj = DemoClass()

obj.read_number()

Source: https://beginnersbook.com/2018/03/python-constructors-default-and-parameterized/

**12. Factory**
<br>

**13.	Decorator**
<br>
Decorators modify the behavior of function or class. Decorators allow to wrap another function in order to extend 
the behavior of wrapped function, without permanently modifying it.

Example: 
 
Source: https://www.geeksforgeeks.org/decorators-in-python/

**14.	Extend Class**
<br>

**15.	CSV Files**
<br>

A Comma Separated Values file (CSV) a plain text data only file. It separates the data values with a delimiter of a 
comma within the file. 
Example of file contents:
column 1 name,column 2 name, column 3 name
first row data 1,first row data 2,first row data 3
second row data 1,second row data 2,second row data 3

Source: https://realpython.com/python-csv/
 
**16.	Reading Files**
<br>
In order to read a file such as a CSV file, an object reader would need to be added. 
Example object reader: 
import csv

with open('employee_birthday.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')

Source:  https://realpython.com/python-csv/
