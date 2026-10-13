import pytest
from uuid import UUID

from domain.models.area import Area


def test_create_area():
    """Se puede crear un área válida"""
    area = Area.create("Francesa")
    assert area.name == "Francesa"
    assert isinstance(area.id, UUID)


def test_area_strips_name():
    """Se eliminan los espacios exteriores del nombre"""
    area = Area.create("  Francesa  ")
    assert area.name == "Francesa"


def test_area_rejects_empty_name():
    """El nombre no puede estar vacío"""
    with pytest.raises(ValueError):
        Area.create("")


def test_area_rejects_whitespace_name():
    """El nombre no puede contener únicamente espacios en blanco"""
    with pytest.raises(ValueError):
        Area.create("   ")