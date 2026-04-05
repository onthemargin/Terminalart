from generators.base import AsciiGenerator


class RabbitGenerator(AsciiGenerator):
    """Generator for ASCII rabbit art."""

    @property
    def name(self) -> str:
        return "Rabbit"

    @property
    def description(self) -> str:
        return "A cute rabbit"

    @property
    def fun_facts(self) -> list[str]:
        return [
            "Rabbits can't vomit — so they eat lots of fiber to stay healthy!",
            "A happy rabbit will jump and twist in the air — it's called a 'binky'!",
            "Rabbits' teeth never stop growing.",
            "Baby rabbits are called 'kittens' — just like baby cats!",
            "Rabbits can see almost 360 degrees around them.",
        ]

    def generate(self) -> str:
        return r"""[white]    ((\((\
    ((  -.- ))
    oo__("")(""))[/white]"""
