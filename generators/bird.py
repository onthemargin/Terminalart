from generators.base import AsciiGenerator


class BirdGenerator(AsciiGenerator):
    """Generator for ASCII bird art."""

    @property
    def name(self) -> str:
        return "Bird"

    @property
    def description(self) -> str:
        return "A flying bird"

    def generate(self) -> str:
        return """[blue]    ____
  >(o )__
   (  ._>
    `--[/blue]"""
