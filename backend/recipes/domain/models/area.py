from repositories.interface_identifiable import Identifiable
from database.base import Base

from uuid import UUID, uuid4
from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from recipes.domain.models.recipe import Recipe

class Area(Identifiable, Base):

    __tablename__ = "areas"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)

    recipes: Mapped[list["Recipe"]] = relationship(back_populates="area")

    def get_id(self) -> UUID:
        return self.id