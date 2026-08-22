from database.base import Base
from recipes.domain.models.ingredient import IngredientUnit

from decimal import Decimal
from uuid import UUID
from typing import TYPE_CHECKING

from sqlalchemy import Enum
from sqlalchemy import Numeric, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from recipes.domain.models.recipe import Recipe
    from recipes.domain.models.ingredient import Ingredient

class RecipeIngredient(Base):
    __tablename__ = "recipe_ingredient"

    recipe_id: Mapped[UUID] = mapped_column(ForeignKey("recipes.id"), primary_key=True)
    ingredient_id: Mapped[UUID] = mapped_column(ForeignKey("ingredients.id"), primary_key=True)
    quantity: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    unit: Mapped[IngredientUnit] = mapped_column(Enum(IngredientUnit), nullable=False)

    recipe: Mapped["Recipe"] = relationship(back_populates="recipe_ingredients")
    ingredient: Mapped["Ingredient"] = relationship(back_populates="recipe_ingredients")