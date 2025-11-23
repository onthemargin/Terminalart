from generators.base import AsciiGenerator


class FishGenerator(AsciiGenerator):
    """Generator for ASCII fish art."""

    @property
    def name(self) -> str:
        return "Fish"

    @property
    def description(self) -> str:
        return "A swimming fish"

    def generate(self) -> str:
        return """[cyan]>>><<<(((((((°°°>>>[/cyan]"""
