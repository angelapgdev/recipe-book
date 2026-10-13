from dataclasses import dataclass
from uuid import UUID, uuid4

from .entity import Entity


@dataclass
class Category(Entity):
    id: UUID
    name: str

    @classmethod
    def create(cls, name: str) -> "Category":
        name = name.strip()

        if not name:
            raise ValueError("Category name cannot be empty")

        return cls(
            id=uuid4(),
            name=name
        )

    def get_id(self) -> UUID:
        return self.id