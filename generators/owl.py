from generators.base import AsciiGenerator


class OwlGenerator(AsciiGenerator):
    """Generator for ASCII owl art."""

    @property
    def name(self) -> str:
        return "Owl"

    @property
    def description(self) -> str:
        return "A wise owl"

    def generate(self) -> str:
        return r"""[yellow]   ,___,
  (O,O)
  (   )
   ---[/yellow]"""
