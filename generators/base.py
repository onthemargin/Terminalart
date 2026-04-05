from abc import ABC, abstractmethod


class AsciiGenerator(ABC):
    """Base class for ASCII art generators."""

    @abstractmethod
    def generate(self) -> str:
        """Generate and return ASCII art with optional color markup.

        Uses Rich markup for colors:
        - [red]text[/red]
        - [blue]text[/blue]
        - [cyan]text[/cyan]
        etc.

        Returns:
            ASCII art string with optional color markup
        """
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        """Display name for this generator."""
        pass

    @property
    def description(self) -> str:
        """Optional description of the ASCII art."""
        return ""

    @property
    def fun_facts(self) -> list[str]:
        """Fun facts about this animal for kids."""
        return []
