from generators.base import AsciiGenerator


class FrogGenerator(AsciiGenerator):
    """Generator for ASCII frog art."""

    @property
    def name(self) -> str:
        return "Frog"

    @property
    def description(self) -> str:
        return "A jumping frog"

    @property
    def fun_facts(self) -> list[str]:
        return [
            "Frogs drink water through their skin — they never actually 'drink'!",
            "A group of frogs is called an 'army'.",
            "Some frogs can freeze solid in winter and thaw back to life in spring!",
            "The golden poison frog has enough toxin to take down 10 grown humans.",
            "Frogs have been on Earth for over 200 million years!",
        ]

    def generate(self) -> str:
        return """[green]   @..@
  (----)
 ( >__< )
 ^^  ~~  ^^[/green]"""
