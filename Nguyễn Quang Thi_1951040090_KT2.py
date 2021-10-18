from random import Random, random

        
class HUMAN:
    def __init__(self, age=None, gender=None):
        if age is not None:
            self._age = age
        else:
            self._age = Random.randint(0, 160)
            Random.ran
        if gender is not None:
            self._gender = gender
        else:
            self._gender = Random.choice(['female', 'male'])


    def age(self):
        return self._age

    def gender(self):
        return self._gender

    def eat(self):
        pass
    def sleep(self):
        pass
    def run(self):
        pass


class STUDENT(HUMAN):

    def __init__(self, age=None, gender=None, id=None, grade=None, credits=None):
        super().__init__(age, gender)
        #Using instance's attribute, not Class Attribute here
        self._complex_list = []
        if age is not None:
            self._age = age
        else:
            self._age = random.randint(18, 28)
        if id is not None:
            self._id = id
        else:
            self._id = Random.randint(0, 9999)
        if credits is not None:
            self._credits = credits
        else:
            self._credits = Random.randrange(0, 250)
        if grade is not None:
            self._grade = grade
        else:
            self._grade = Random.randint(0, 4)
    def id(self):
        return self._id

    def credits(self):
        return self._credits

    def grade(self):
        return self._grade

    def complex_list(self):
        return self._complex_list

    def result(self):
        if self._grade > 3.8 and self._grade < 4 :
              return 'A+'
        elif self._grade < 3.5 and self._grade > 3.3 :
                return 'A'
        elif self._grade > 3 and self._grade < 3.2 :
            return 'B+'
        elif self._grade > 2.6 and self._grade < 2.9 :
            return 'B'
        elif self._grade > 1.8 and self._grade < 2.5 :
            return 'C'
        elif self._grade < 1.8 :
            return 'D'
        def graduate(result, self):
            if result != 'D' and self._credit == 250 :
                return True
            else:
                return False
                