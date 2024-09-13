from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    city: str = "Unknown"  # Default value

# Creating an instance of the dataclass
person = Person(name="Alice", age=30, city = "Hayward")

print(person)  # Output: Person(name='Alice', age=30, city='Unknown')