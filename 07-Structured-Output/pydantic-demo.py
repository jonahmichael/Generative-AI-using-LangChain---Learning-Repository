from pydantic import BaseModel,EmailStr,Field
from typing import Optional # Basemodel contains validation logic

# Here we define the output structure using Pydantic model
class ReviewAnalysis(BaseModel): 
  name: str = 'Unknown'  # Default value if name is not provided
  age: Optional[int] = 0  # Default value if age is not provided
                          # Optional field with default value
                          
  email: Optional[EmailStr] = None  # Optional email field with validation
  cgpa: float=Field(gt=0,lt=10,description="CGPA should be between 0 and 10") # Field with constraints and description


new_student={"age":21,"email":"john.doe@example.com"}  # Example dictionary matching the model fields
student = ReviewAnalysis(**new_student) # Unpacking the dictionary to match the model fields 
print(student)