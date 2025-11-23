from generators.base import AsciiGenerator


class CatGenerator(AsciiGenerator):
    """Generator for ASCII cat art."""

    @property
    def name(self) -> str:
        return "Cat"

    @property
    def description(self) -> str:
        return "A cute cat"

    def generate(self) -> str:
        return """   /\\_/\\
  ( o.o )
   > ^ <
  /|   |\\"""
