"""Tests for the GeneratorRegistry."""

import pytest
from generators.base import AsciiGenerator
from generators.registry import GeneratorRegistry
from generators.cat import CatGenerator
from generators.dog import DogGenerator
from generators.bird import BirdGenerator
from generators.fish import FishGenerator
from generators.butterfly import ButterflyGenerator
from generators.rabbit import RabbitGenerator
from generators.snake import SnakeGenerator
from generators.frog import FrogGenerator
from generators.owl import OwlGenerator


@pytest.fixture
def registry():
    return GeneratorRegistry()


class TestRegistryInit:
    def test_has_exactly_nine_generators(self, registry):
        assert len(registry.get_all()) == 9


class TestGetAll:
    def test_returns_list(self, registry):
        result = registry.get_all()
        assert isinstance(result, list)

    def test_all_items_are_ascii_generators(self, registry):
        for gen in registry.get_all():
            assert isinstance(gen, AsciiGenerator)

    def test_returns_nine_generators(self, registry):
        assert len(registry.get_all()) == 9

    def test_all_names_unique(self, registry):
        names = [g.name for g in registry.get_all()]
        assert len(names) == len(set(names))


EXPECTED_LOOKUPS = [
    ("Cat", CatGenerator),
    ("Dog", DogGenerator),
    ("Bird", BirdGenerator),
    ("Fish", FishGenerator),
    ("Butterfly", ButterflyGenerator),
    ("Rabbit", RabbitGenerator),
    ("Snake", SnakeGenerator),
    ("Frog", FrogGenerator),
    ("Owl", OwlGenerator),
]


class TestGetByName:
    @pytest.mark.parametrize("name,expected_cls", EXPECTED_LOOKUPS,
                             ids=[name for name, _ in EXPECTED_LOOKUPS])
    def test_returns_correct_generator(self, registry, name, expected_cls):
        gen = registry.get_by_name(name)
        assert gen is not None
        assert isinstance(gen, expected_cls)

    def test_nonexistent_returns_none(self, registry):
        assert registry.get_by_name("nonexistent") is None

    def test_case_sensitive(self, registry):
        assert registry.get_by_name("cat") is None

    def test_empty_string_returns_none(self, registry):
        assert registry.get_by_name("") is None
