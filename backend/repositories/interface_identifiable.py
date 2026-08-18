from abc import ABC, abstractmethod
import uuid

class Identifiable(ABC):
    """Exige que el repositorio ofrezca métodos get para gestionar el identificador."""

    @abstractmethod
    def get_id() -> uuid:
        pass