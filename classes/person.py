class Person:
    """
    person first_name, last_name, age
    """
    def __init__(self, first_name=None, last_name=None):
        self.first_name = first_name
        self.last_name = last_name
    
    # def __str__ (self):
    #     return f"Hello, testing str header first name: {self.first_name} | last name: {self.last_name} | age: {self.age}"

    def __repr__ (self):
        return f"first name: {self.first_name} | last name: {self.last_name}"
    

# alic = Person("Alice", "Lee", "15")
# bob = Person("Bob", "Roger", 24)

# print(alic)
# print(bob)
# print([alic, bob])