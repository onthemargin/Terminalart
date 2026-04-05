from generators.base import AsciiGenerator


class BirdGenerator(AsciiGenerator):
    """Generator for ASCII bird art."""

    @property
    def name(self) -> str:
        return "Bird"

    @property
    def description(self) -> str:
        return "A flying bird"

    @property
    def fun_facts(self) -> list[str]:
        return [
            "Hummingbirds can fly backwards — they're the only birds that can!",
            "A flamingo can only eat with its head upside down.",
            "Penguins propose to their mates with a pebble.",
            "An ostrich's eye is bigger than its brain!",
            "Crows can recognize human faces and remember them for years.",
        ]

    def generate(self) -> str:
        return """[blue]    ____
  >(o )__
   (  ._>
    `--[/blue]"""
