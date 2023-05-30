class Student:
    company='IBM'

    @staticmethod
    def add(a,b):
        c=a+b
        print('{0}+{1}={2}'.format(a,b,c))
        return c

Student.add(2,3)

class Student1:
    company='IBM'

    @classmethod
    def add(cls,a,b):
        c=a+b
        print('{0}+{1}={2}'.format(a,b,c))
        return c

Student1.add(12,13)
