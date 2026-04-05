from generators.base import AsciiGenerator


class OwlGenerator(AsciiGenerator):
    """Generator for ASCII owl art."""

    @property
    def name(self) -> str:
        return "Owl"

    @property
    def description(self) -> str:
        return "A wise owl"

    @property
    def fun_facts(self) -> list[str]:
        return [
            "Owls can rotate their heads up to 270 degrees!",
            "A group of owls is called a 'parliament'.",
            "Owls' eyes are so big they can't move them — that's why they turn their heads.",
            "Barn owls can hear a mouse's heartbeat from 30 feet away.",
            "Some owls have ear tufts that aren't actually ears at all!",
        ]

    def generate(self) -> str:
        return r"""[yellow]   ,___,
  (O,O)
  (   )
   ---[/yellow]"""
