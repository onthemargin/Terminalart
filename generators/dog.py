from generators.base import AsciiGenerator


class DogGenerator(AsciiGenerator):
    """Generator for ASCII dog art."""

    @property
    def name(self) -> str:
        return "Dog"

    @property
    def description(self) -> str:
        return "A friendly dog"

    def generate(self) -> str:
        return """[yellow]   //  \\___
  (((  @@@\\___
  //      OO
 //__((__//[/yellow]"""
