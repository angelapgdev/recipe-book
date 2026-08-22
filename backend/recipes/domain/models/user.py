from repositories.interface_identifiable import Identifiable
from database.base import Base

from uuid import UUID, uuid4
from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from recipes.domain.models.recipe import Recipe
    from recipes.domain.models.fridge import Fridge

class User(Identifiable, Base):

    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    pssw_hash: Mapped[str] = mapped_column(String(100), nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False)

    recipes: Mapped[list["Recipe"]] = relationship(back_populates="user")
    fridges: Mapped[list["Fridge"]] = relationship(back_populates="user")


    def get_id(self) -> UUID:
        return self.id