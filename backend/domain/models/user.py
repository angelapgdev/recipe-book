from dataclasses import dataclass
from uuid import UUID, uuid4
import re

from .entity import Entity

EMAIL_PATTERN = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"

def is_valid_email(email: str) -> bool:
    return bool(re.fullmatch(EMAIL_PATTERN, email))

@dataclass
class User(Entity):
    id: UUID
    email: str
    password_hash: str
    name: str

    @classmethod
    def create(cls, email:str, password_hash: str, name: str) -> "User" :
        name = name.strip()
        email = email.strip()
        password_hash = password_hash.strip()

        if not name:
            raise ValueError("User name cannot be empty")

        if not is_valid_email(email):
            raise ValueError("User email is not valid")

        if not password_hash:
            raise ValueError("User password hash cannot be empty")
        
        return cls(
            id=uuid4(),
            email=email,
            password_hash=password_hash,
            name=name
        )
    
    def get_id(self) -> UUID:
        return self.id
