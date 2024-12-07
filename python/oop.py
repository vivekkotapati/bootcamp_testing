class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Call Parent's constructor
        self.age = age
s=hi("vivek")
print(s.name)