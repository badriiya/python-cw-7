
# write your code here
class Person:
    # name = "badriya"
    # age = 21
    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def is_adult(self):
        if self.age > 18:
            print("You have too much responsibilities")
        elif self.age < 18:
            print("Lucky you")

    def __str__(self):
        return f"My name is {self.name} and I am {self.age} years old "

first_person = Person("badriya", 21)
print(first_person.age, first_person.name)
first_person.is_adult()

print(first_person)
