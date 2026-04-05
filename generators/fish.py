from generators.base import AsciiGenerator


class FishGenerator(AsciiGenerator):
    """Generator for ASCII fish art."""

    @property
    def name(self) -> str:
        return "Fish"

    @property
    def description(self) -> str:
        return "A swimming fish"

    @property
    def fun_facts(self) -> list[str]:
        return [
            "There are over 30,000 known species of fish!",
            "A seahorse is one of the slowest fish — it would take 1 hour to travel 150 meters.",
            "Clownfish can change from male to female!",
            "Fish can feel pain and have memories that last months.",
            "The oldest known fish lived to be 112 years old!",
        ]

    def generate(self) -> str:
        return """[cyan]>>><<<(((((((°°°>>>[/cyan]"""
