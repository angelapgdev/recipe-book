from repositories.interface_identifiable import Identifiable
from database.base import Base

from enum import Enum
from uuid import UUID, uuid4
from typing import TYPE_CHECKING

from sqlalchemy import Enum as SQLEnum
from sqlalchemy import String, JSON, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from recipes.domain.models.category import Category
    from recipes.domain.models.area import Area
    from recipes.domain.models.user import User
    from recipes.domain.models.ingredient_recipe import RecipeIngredient

class RecipeDifficulty(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class Recipe(Identifiable, Base):

    __tablename__ = "recipes"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    difficulty: Mapped[RecipeDifficulty|None] = mapped_column(SQLEnum(RecipeDifficulty), nullable=True)
    minutes: Mapped[int|None] = mapped_column(nullable=True)
    image_path: Mapped[str|None] = mapped_column(String(500), nullable=True)
    steps: Mapped[list[str]] = mapped_column(JSON, nullable=False)

    category_id: Mapped[UUID] = mapped_column(ForeignKey("categories.id"), nullable=False)
    area_id: Mapped[UUID|None] = mapped_column(ForeignKey("areas.id"), nullable=True)
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"), nullable=False)

    category: Mapped["Category"] = relationship(back_populates="recipes")
    area: Mapped["Area|None"] = relationship(back_populates="recipes")
    user: Mapped["User"] = relationship(back_populates="recipes")

    recipe_ingredients: Mapped[list["RecipeIngredient"]] = relationship(back_populates="recipe")


    def get_id(self) -> UUID:
        return self.id