from database.base import Base
from recipes.domain.models.ingredient import IngredientUnit

from decimal import Decimal
from uuid import UUID
from typing import TYPE_CHECKING

from sqlalchemy import Enum
from sqlalchemy import Numeric, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from recipes.domain.models.fridge import Fridge
    from recipes.domain.models.ingredient import Ingredient

class FridgeIngredient(Base):
    __tablename__ = "fridge_ingredient"

    fridge_id: Mapped[UUID] = mapped_column(ForeignKey("fridges.id"), primary_key=True)
    ingredient_id: Mapped[UUID] = mapped_column(ForeignKey("ingredients.id"), primary_key=True)
    quantity: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    unit: Mapped[IngredientUnit] = mapped_column(Enum(IngredientUnit), nullable=False)

    fridge: Mapped["Fridge"] = relationship(back_populates="fridge_ingredients")
    ingredient: Mapped["Ingredient"] = relationship(back_populates="fridge_ingredients")