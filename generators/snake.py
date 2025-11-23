from generators.base import AsciiGenerator


class SnakeGenerator(AsciiGenerator):
    """Generator for ASCII snake art."""

    @property
    def name(self) -> str:
        return "Snake"

    @property
    def description(self) -> str:
        return "A slithering snake"

    def generate(self) -> str:
        return """[green]      ,,,---
,,,---'''
```===eee[/green]"""
