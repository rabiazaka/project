class Person():
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
        def sit(self):
            """Simulate a dog sitting in response to a command."""
            print(self.name.title() + " is now sitting.")
        def roll_over(self):
            """Simulate rolling over in response to a command."""
            print(self.name.title() + " rolled over!")
person=Person('sara',6)
print("my name is " + person.name.title()+".")
print("my age is " + str(person.age)+" years old.")
