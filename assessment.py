"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   Abstraction: It allows to hide complex details (inside the object) to focus more in its functionality. 
   Encapsulation: It allows to put several functionalities together.
   Polymorphism: It allows to create different objects with interchangeable components.  

2. What is a class?

    It's an abstraction (idea) that groups elements with characteristics in common without being the exact same. 
    These characteristics in common, which can be attributes and methods, can be "personalized" at an instance level. 
    Attributes and methods are encapculated within the class and can be used by objects of the same class or its subclasses.

3. What is an instance attribute?
    
    It's an attribute defined at an instance (object) level, when instantiated.
    If not specified, the object inherites the attribute defined by its class.

4. What is a method?
    
    It's a function specified for an instance of a certain class.

5. What is an instance in object orientation?

    It's a particular entity that belongs to a class.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

   Class attributes are common to all instances that belong to a certain class, while
   instance attributes are defined for aa particular instance of that class.

   Example:
   If we define a class Cars, all instances in Cars have 4 tires, windows, a wheel--those are class attributes.
   However, some cars have 2 doors (while others, 4), some are electric (while others are not), some might even
   be self-driven --those particular characteristics, not common to all instances in the same class, are instance
   attributes.
"""


# Parts 2 through 5:
# Create your classes and class methods
class Student(object):
    """
    """
    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

class Question(object):
    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        users_answer = raw_input(self.question)
        return users_answer == self.correct_answer

class AbstractTest(object):
    """ In this assessment, it can either be an exam or a quiz. 
    Depending on the type, it returns a number or a boolean.
    The attribute 'questions' is a list of elements whose class is Question 
    (that have 'question' and 'correct_answer' as attributes
    """

    test_type = 'exam'
    def __init__(self, name, test_type = None):
        self.name = name
        self.questions = []
        if test_type:
            self.test_type = test_type

    def add_question(self, question, correct_answer):
        self.questions.append(Question(question, correct_answer))

    def administer(self):
        #each element of self.questions is an instance of the Question class
        score = 0.0
        for qs in self.questions:
            if qs.ask_and_evaluate():
                score = score + 1.0

        if self.test_type == 'exam':
            return float("{0:.2f}".format(score/(len(self.questions))))
        else:
            return score/(len(self.questions)) >= 0.5

class Exam(AbstractTest):
    test_type = 'exam'



class Quiz(AbstractTest):
    test_type = 'quiz'



def take_test(exam, student):
    """ takes exam and student instances (from Exam and Student classes, respectively)
    and adds the attribute 'score' to the student instance. Also, shows said score. 
    """
    student.score = exam.administer() #passing an instance attribute
    print student.score

def example():
    """Creates an exam, 
    adds questions,
    creates a student,
    administers the exam"""
    exam1 = Exam('midterm')
    exam1.add_question('What is the method for adding an element to a set (.name())? ', '.add()')
    exam1.add_question('What is the method for adding an element to a list? (.name()) ', '.append()')
    exam1.add_question('Lists can be dictionary keys, true or false? ', 'false')
    exam1.add_question('Sets are mutable, true or false? ', 'false')
    student1 = Student('Erika', 'Azabache', 'Nowhere road 666')
    take_test(exam1, student1)
    return

example()

