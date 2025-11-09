from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int
    email: str
    
newperson: Person = {
    "name": "Jonah",   
    "age": 19,
    "email": "jonah@example.com"
}

print(newperson)
# Example of using TypedDict to define a structured output for a person with name, age, and email fields.
# Example usage of TypedDict to define structured output