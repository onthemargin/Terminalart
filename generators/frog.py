from generators.base import AsciiGenerator


class FrogGenerator(AsciiGenerator):
    """Generator for ASCII frog art."""

    @property
    def name(self) -> str:
        return "Frog"

    @property
    def description(self) -> str:
        return "A jumping frog"

    def generate(self) -> str:
        return """[green]   @..@
  (----)
 ( >__< )
 ^^  ~~  ^^[/green]"""
