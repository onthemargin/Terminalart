from generators.base import AsciiGenerator


class RabbitGenerator(AsciiGenerator):
    """Generator for ASCII rabbit art."""

    @property
    def name(self) -> str:
        return "Rabbit"

    @property
    def description(self) -> str:
        return "A cute rabbit"

    def generate(self) -> str:
        return r"""[white]    ((\((\
    ((  -.- ))
    oo__("")(""))[/white]"""
