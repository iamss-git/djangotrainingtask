class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

@classmethod
def obj_createwithage_by_yr(cls, name, year):
    age = date.today().year - year
    print(age)

    return cls(name, age)

person = Person("liza", 22)

P2 = Person.obj_createwithage_by_yr("ABC", 1998)