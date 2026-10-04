from abc import ABC, abstractmethod
from uuid import UUID


class Entity(ABC):

    @abstractmethod
    def get_id(self) -> UUID:
        pass