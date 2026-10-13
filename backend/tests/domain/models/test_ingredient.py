import pytest
from uuid import UUID

from domain.models.ingredient import Ingredient


def test_create_ingredient():
    """Se puede crear un ingrediente válido"""
    ingredient = Ingredient.create("Tomate")
    assert ingredient.name == "Tomate"
    assert isinstance(ingredient.id, UUID)


def test_ingredient_strips_name():
    """Se eliminan los espacios exteriores del nombre"""
    ingredient = Ingredient.create("  Tomate  ")
    assert ingredient.name == "Tomate"


def test_ingredient_rejects_empty_name():
    """El nombre no puede estar vacío"""
    with pytest.raises(ValueError):
        Ingredient.create("")


def test_ingredient_rejects_whitespace_name():
    """El nombre no puede contener únicamente espacios en blanco"""
    with pytest.raises(ValueError):
        Ingredient.create("   ")