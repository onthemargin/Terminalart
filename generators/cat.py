from generators.base import AsciiGenerator


class CatGenerator(AsciiGenerator):
    """Generator for ASCII cat art."""

    @property
    def name(self) -> str:
        return "Cat"

    @property
    def description(self) -> str:
        return "A cute cat"

    @property
    def fun_facts(self) -> list[str]:
        return [
            "Cats sleep for about 13-16 hours a day!",
            "A group of cats is called a 'clowder'.",
            "Cats can rotate their ears 180 degrees.",
            "Cats have over 20 different vocalizations, including the purr!",
            "A cat's purr vibrates at 25-150 Hz, which can help heal bones.",
        ]

    def generate(self) -> str:
        return """[white]   /\\_/\\
  ( o.o )
   > ^ <
  /|   |\\[/white]"""
