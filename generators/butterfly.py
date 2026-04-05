from generators.base import AsciiGenerator


class ButterflyGenerator(AsciiGenerator):
    """Generator for ASCII butterfly art."""

    @property
    def name(self) -> str:
        return "Butterfly"

    @property
    def description(self) -> str:
        return "A colorful butterfly"

    @property
    def fun_facts(self) -> list[str]:
        return [
            "Butterflies taste with their feet!",
            "Monarch butterflies migrate up to 3,000 miles every year.",
            "A butterfly's wings are actually transparent — the colors come from tiny scales.",
            "Butterflies can see colors that humans can't, including ultraviolet!",
            "Some butterflies drink the tears of turtles for nutrients.",
        ]

    def generate(self) -> str:
        return """[magenta]  (\\_/)
 (o.o)
  >*<[/magenta]"""
