import pytest
from uuid import UUID

from domain.models.category import Category


def test_create_category():
    """Se puede crear una categoría válida"""
    category = Category.create("Postres")
    assert category.name == "Postres"
    assert isinstance(category.id, UUID)


def test_category_strips_name():
    """Se eliminan los espacios exteriores del nombre"""
    category = Category.create("  Postres  ")
    assert category.name == "Postres"


def test_category_rejects_empty_name():
    """El nombre no puede estar vacío"""
    with pytest.raises(ValueError):
        Category.create("")


def test_category_rejects_whitespace_name():
    """El nombre no puede contener únicamente espacios en blanco"""
    with pytest.raises(ValueError):
        Category.create("   ")