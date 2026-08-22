from repositories.interface_identifiable import Identifiable
from database.base import Base

from uuid import UUID, uuid4
from typing import TYPE_CHECKING

from sqlalchemy import String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from recipes.domain.models.user import User
    from recipes.domain.models.ingredient_fridge import FridgeIngredient

class Fridge(Identifiable, Base):

    __tablename__ = "fridges"

    __table_args__ = (
        UniqueConstraint("user_id", "name", name="uq_fridge_user_name"),
    )

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column(String(100), nullable=False)

    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"), nullable=False)

    user: Mapped["User"] = relationship(back_populates="fridges")

    fridge_ingredients: Mapped[list["FridgeIngredient"]] = relationship(back_populates="fridge")


    def get_id(self) -> UUID:
        return self.id