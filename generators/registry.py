from generators.base import AsciiGenerator
from generators.dog import DogGenerator
from generators.cat import CatGenerator
from generators.bird import BirdGenerator
from generators.fish import FishGenerator
from generators.butterfly import ButterflyGenerator
from generators.rabbit import RabbitGenerator
from generators.snake import SnakeGenerator
from generators.frog import FrogGenerator
from generators.owl import OwlGenerator


class GeneratorRegistry:
    """Registry for all available ASCII generators."""

    def __init__(self):
        self._generators = []
        self._register_defaults()

    def _register_defaults(self):
        """Register default generators."""
        self._generators.append(DogGenerator())
        self._generators.append(CatGenerator())
        self._generators.append(BirdGenerator())
        self._generators.append(FishGenerator())
        self._generators.append(ButterflyGenerator())
        self._generators.append(RabbitGenerator())
        self._generators.append(SnakeGenerator())
        self._generators.append(FrogGenerator())
        self._generators.append(OwlGenerator())

    def get_all(self) -> list[AsciiGenerator]:
        """Get all registered generators."""
        return self._generators

    def get_by_name(self, name: str) -> AsciiGenerator | None:
        """Get generator by name."""
        for gen in self._generators:
            if gen.name == name:
                return gen
        return None
