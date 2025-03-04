from pydantic import BaseModel, EmailStr

class UserModel(BaseModel):
    name: str
    email: EmailStr  # Ensures email format is correct


#✅ This ensures incoming API data is properly formatted before inserting into the database.

