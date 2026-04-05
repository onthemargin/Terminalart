from generators.base import AsciiGenerator


class SnakeGenerator(AsciiGenerator):
    """Generator for ASCII snake art."""

    @property
    def name(self) -> str:
        return "Snake"

    @property
    def description(self) -> str:
        return "A slithering snake"

    @property
    def fun_facts(self) -> list[str]:
        return [
            "Snakes smell with their tongues!",
            "Some snakes can fly — they flatten their bodies and glide between trees.",
            "Snakes don't have eyelids — they sleep with their eyes open!",
            "The longest snake ever found was a python over 25 feet long.",
            "Snakes can eat things 75-100% bigger than their own head.",
        ]

    def generate(self) -> str:
        return """[green]      ,,,---
,,,---'''
```===eee[/green]"""
