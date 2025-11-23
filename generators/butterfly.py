from generators.base import AsciiGenerator


class ButterflyGenerator(AsciiGenerator):
    """Generator for ASCII butterfly art."""

    @property
    def name(self) -> str:
        return "Butterfly"

    @property
    def description(self) -> str:
        return "A colorful butterfly"

    def generate(self) -> str:
        return """[magenta]  (\\_/)
 (o.o)
  >*<[/magenta]"""
