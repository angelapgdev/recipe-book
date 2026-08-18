from repositories.interface_repository import Repository
from abc import ABC
from uuid import UUID

class UUIDRepository[T](Repository[T, UUID], ABC):
    pass