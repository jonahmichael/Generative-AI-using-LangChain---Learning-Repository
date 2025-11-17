# Structured outputs in langchain

# Ways to get structured outputs:

# 1. with_structured_output (can generate structured output by its own eg: OpenAI)
# 2. Output Parsers (for models that don't have built-in structured output capabilities)

# 1. with_structured_output

# Before invoking the model, we can specify the desired output format using the with_structured_output method.
# These can be done 3 ways:

# a) TypedDict - Define a TypedDict to specify the structure of the output. eg: JSON-like structure.

# b) Pydantic Model - Use a Pydantic model to define the output structure. eg: more complex validation and parsing.

# c) JSON Schema - Define the output structure using a JSON schema. eg: widely used standard for defining data structures.

# ---------------------------------------------

# When to use which?

# TypedDict - Use when you need a simple and straightforward way to define the output structure without additional validation.

# Pydantic Model - Use when you require more complex validation, parsing, and data manipulation capabilities.
# JSON Schema - Use when you want a widely recognized standard for defining data structures, especially if interoperability with other systems is a concern.

# Pydantic, TypedDict, and JSON Schema are all used for data validation and defining data structures, but they have different use cases and work at different stages of development.

# 1. TypedDict: For static type checking
# Use TypedDict when you want to provide type hints for a dictionary with a fixed set of string keys.
# It's a way to help static type checkers (like MyPy) and your IDE understand the structure of your dictionaries, which can help you catch bugs before you run your code.
# It does not perform any runtime validation. It's like a set of rules on paper that you hope everyone follows.

from typing import TypedDict

class User(TypedDict):
    name: str
    id: int

# This will pass static analysis, but at runtime, there's nothing stopping you from creating a dictionary that doesn't match the TypedDict definition.
user: User = {"name": "Alice", "id": 1}

# 2. Pydantic: For runtime data validation, parsing, and serialization
# Use Pydantic when you need to validate data at runtime, especially when it's coming from an external source like an API request or a JSON file.
# Pydantic enforces the data structure and types at runtime. If the data doesn't conform to the model, Pydantic will raise a validation error.
# It can also coerce data into the correct types (e.g., converting a string to a number).
# Pydantic models are also used for serializing data into JSON and can generate JSON Schemas.

from pydantic import BaseModel, ValidationError

class PydanticUser(BaseModel):
    name: str
    id: int

# This will work and create a PydanticUser object
try:
    pydantic_user = PydanticUser(name="Bob", id=2)
except ValidationError as e:
    print(e)

# This will raise a validation error at runtime because 'id' is a string, not an integer.
try:
    invalid_user = PydanticUser(name="Charlie", id="not-an-int")
except ValidationError as e:
    print(e)

# 3. JSON Schema: A language-agnostic standard for validating JSON data
# Use JSON Schema to define the structure and validation rules for JSON documents in a language-independent way.
# It's a declarative language for annotating and validating JSON documents.
# Pydantic can generate a JSON Schema from a Pydantic model, which is useful for things like generating OpenAPI documentation for an API.

# You can get the JSON Schema for the PydanticUser model like this:
schema = PydanticUser.model_json_schema()
# print(schema) # This would print the generated JSON schema

# In summary:
# - Use TypedDict for static analysis and to provide type hints for dictionaries.
# - Use Pydantic for runtime validation, data parsing, and serialization, especially for data from external sources.
# - Use JSON Schema as a language-agnostic way to describe and validate JSON data structures, often in conjunction with tools like Pydantic for API documentation and validation.
