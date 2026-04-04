"""Tests for individual ASCII art generators."""

import re
import pytest
from generators.base import AsciiGenerator
from generators.cat import CatGenerator
from generators.dog import DogGenerator
from generators.bird import BirdGenerator
from generators.fish import FishGenerator
from generators.butterfly import ButterflyGenerator
from generators.rabbit import RabbitGenerator
from generators.snake import SnakeGenerator
from generators.frog import FrogGenerator
from generators.owl import OwlGenerator

# Rich markup pattern: [color]...[/color]
RICH_MARKUP_RE = re.compile(r"\[/?\w+\]")

ALL_GENERATORS = [
    CatGenerator,
    DogGenerator,
    BirdGenerator,
    FishGenerator,
    ButterflyGenerator,
    RabbitGenerator,
    SnakeGenerator,
    FrogGenerator,
    OwlGenerator,
]


@pytest.fixture(params=ALL_GENERATORS, ids=lambda cls: cls.__name__)
def generator(request):
    """Yield each generator instance in turn."""
    return request.param()


class TestGeneratorInterface:
    """Every generator must satisfy the AsciiGenerator contract."""

    def test_is_ascii_generator(self, generator):
        assert isinstance(generator, AsciiGenerator)

    def test_name_is_non_empty_string(self, generator):
        assert isinstance(generator.name, str)
        assert len(generator.name) > 0

    def test_description_is_non_empty_string(self, generator):
        assert isinstance(generator.description, str)
        assert len(generator.description) > 0

    def test_generate_returns_non_empty_string(self, generator):
        result = generator.generate()
        assert isinstance(result, str)
        assert len(result) > 0

    def test_generate_contains_rich_markup(self, generator):
        result = generator.generate()
        assert RICH_MARKUP_RE.search(result), (
            f"{generator.name} generate() should contain Rich markup tags "
            f"like [color]...[/color]"
        )


class TestCatGenerator:
    def test_name(self):
        assert CatGenerator().name == "Cat"

    def test_description(self):
        assert CatGenerator().description == "A cute cat"


class TestDogGenerator:
    def test_name(self):
        assert DogGenerator().name == "Dog"

    def test_description(self):
        assert DogGenerator().description == "A friendly dog"


class TestBirdGenerator:
    def test_name(self):
        assert BirdGenerator().name == "Bird"


class TestFishGenerator:
    def test_name(self):
        assert FishGenerator().name == "Fish"


class TestButterflyGenerator:
    def test_name(self):
        assert ButterflyGenerator().name == "Butterfly"


class TestRabbitGenerator:
    def test_name(self):
        assert RabbitGenerator().name == "Rabbit"


class TestSnakeGenerator:
    def test_name(self):
        assert SnakeGenerator().name == "Snake"


class TestFrogGenerator:
    def test_name(self):
        assert FrogGenerator().name == "Frog"


class TestOwlGenerator:
    def test_name(self):
        assert OwlGenerator().name == "Owl"
