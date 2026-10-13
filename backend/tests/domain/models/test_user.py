import pytest
from uuid import UUID

from domain.models.user import User


def test_create_user():
    """Se puede crear un usuario válido"""
    user = User.create("example@email.com", "sdfxjcsn@#dsof1234", "User")
    assert user.email == "example@email.com"
    assert user.password_hash == "sdfxjcsn@#dsof1234"
    assert user.name == "User"
    assert isinstance(user.id, UUID)


def test_user_strips_name():
    """Se eliminan los espacios exteriores del nombre"""
    user = User.create("example@email.com", "sdfxjcsn@#dsof1234", "   User   ")
    assert user.name == "User"


def test_user_rejects_empty_name():
    """El nombre no puede estar vacío"""
    with pytest.raises(ValueError):
        User.create("example@email.com", "sdfxjcsn@#dsof1234", "")


def test_user_rejects_whitespace_name():
    """El nombre no puede contener únicamente espacios en blanco"""
    with pytest.raises(ValueError):
        User.create("example@email.com", "sdfxjcsn@#dsof1234", "   ")


def test_user_strips_email():
    """Se eliminan los espacios exteriores del email."""
    user = User.create(
        "  example@email.com  ",
        "sdfxjcsn@#dsof1234",
        "User"
    )
    assert user.email == "example@email.com"


def test_user_rejects_invalid_email():
    """El email debe ser válido"""
    with pytest.raises(ValueError):
        User.create("example@email.", "sdfxjcsn@#dsof1234", "User")


def test_user_strips_password_hash():
    """Se eliminan los espacios exteriores del hash."""
    user = User.create(
        "example@email.com",
        "  sdfxjcsn@#dsof1234  ",
        "User"
    )
    assert user.password_hash == "sdfxjcsn@#dsof1234"


def test_user_rejects_empty_password_hash():
    """El hash de la contraseña no puede estar vacío."""
    with pytest.raises(ValueError):
        User.create("example@email.com", "", "User")


def test_user_rejects_whitespace_password_hash():
    """El hash de la contraseña no puede contener únicamente espacios."""
    with pytest.raises(ValueError):
        User.create("example@email.com", "   ", "User")