from repositories.interface_identifiable import Identifiable
from database.base import Base

from enum import Enum
from uuid import UUID, uuid4
from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from recipes.domain.models.ingredient_recipe import RecipeIngredient
    from recipes.domain.models.ingredient_fridge import FridgeIngredient

class IngredientUnit(str, Enum):
    UNIT = "unit"
    GRAM = "g"
    KILOGRAM = "kg"
    MILLILITER = "ml"
    LITER = "l"
    TEASPOON = "tsp"
    TABLESPOON = "tbsp"

class Ingredient(Identifiable, Base):

    __tablename__ = "ingredients"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)

    recipe_ingredients: Mapped[list["RecipeIngredient"]] = relationship(back_populates="ingredient")
    fridge_ingredients: Mapped[list["FridgeIngredient"]] = relationship(back_populates="ingredient")

    def get_id(self) -> UUID:
        return self.id