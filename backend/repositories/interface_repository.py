from abc import ABC, abstractmethod

class Repository[T, K](ABC):
    """
    T: tipo de datos que se va a almacenar.
    K: tipo de identificador.
    """

    @abstractmethod
    def add(self, entity: T) -> K:
        """
        Raises:
            RepositoryException: excepción del repositorio.
        """
        pass

    @abstractmethod
    def update(self, entity: T) -> None:
        """
        Raises:
            RepositoryException: excepción del repositorio.
            EntityNotFound: entidad no encontrada.
        """
        pass

    @abstractmethod
    def delete(self, entity: T) -> None:
        """
        Raises:
            RepositoryException: excepción del repositorio.
            EntityNotFound: entidad no encontrada.
        """
        pass

    @abstractmethod
    def get_by_id(self, id: K) -> T:
        """
        Raises:
            RepositoryException: excepción del repositorio.
            EntityNotFound: entidad no encontrada.
        """
        pass

    @abstractmethod
    def get_all(self) -> list[T]:
        """
        Raises:
            RepositoryException: excepción del repositorio.
        """
        pass

    @abstractmethod
    def get_ids(self) -> list[K]:
        """
        Raises:
            RepositoryException: excepción del repositorio.
        """
        pass