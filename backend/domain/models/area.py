from dataclasses import dataclass
from uuid import UUID, uuid4

from .entity import Entity


@dataclass
class Area(Entity):
    id: UUID
    name: str

    @classmethod
    def create(cls, name: str) -> "Area":
        name = name.strip()

        if not name:
            raise ValueError("Area name cannot be empty")

        return cls(
            id=uuid4(),
            name=name
        )

    def get_id(self) -> UUID:
        return self.id