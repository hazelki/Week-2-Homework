"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.
   1. Because it's reuse enables faster development. 
   2.  it comes with libraries of objects and code development
   3. It is s much easier to modify than a non-Object Oriented Program

2. What is a class? It is a logical grouping of data and functions. They can be 
thought of as blueprints for creating objects.


3. What is an instance attribute?
An attribute defined in the instance is an instance attribute
 and is stored in the instance's name space
4. What is a method?
It's a function which is a member of a class. A method is a function that takes a class
 instance as its first parameter.

5. What is an instance in object orientation? it's an object in a class that created 
from a particular class.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.
   Class variables are defined outside of any method of the class. 
   Instance variables are defined inside a method.


"""


# Parts 2 through 5:
# Create your classes and class methods
class Student(object):

	def __init__(self, first_name, last_name, address):

		self.first_name = first_name #instance variable
		self.last_name = last_name
		self. address = address

class Questions(object):
	def __init__(self, question, answer):
	self.question = question
	self.answer = answer

 class Exam(object):
 	def __init__(self, name, question):
 		self.name = name
 		self.question = question

 	def add(self, question, answer):
        self.name = name
        self.questions = questions

    def test(student, exam):




