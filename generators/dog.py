from generators.base import AsciiGenerator


class DogGenerator(AsciiGenerator):
    """Generator for ASCII dog art."""

    @property
    def name(self) -> str:
        return "Dog"

    @property
    def description(self) -> str:
        return "A friendly dog"

    @property
    def fun_facts(self) -> list[str]:
        return [
            "Dogs can smell about 10,000 times better than humans!",
            "A dog's nose print is unique, just like a human fingerprint.",
            "Dogs dream just like people do — you might see their paws twitch!",
            "The tallest dog ever was a Great Dane named Zeus — over 3 feet tall!",
            "Dogs can learn more than 1,000 words.",
        ]

    def generate(self) -> str:
        return """[yellow]   //  \\___
  (((  @@@\\___
  //      OO
 //__((__//[/yellow]"""
